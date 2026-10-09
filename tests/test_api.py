import time
from types import SimpleNamespace
import jwt
import pytest
from fastapi.testclient import TestClient
from cryptography.hazmat.primitives.asymmetric import rsa
from portshield_ai.api import app
from portshield_ai import auth

TOKEN='synthetic-test-token-0123456789'
@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv('AUTH_MODE','demo');monkeypatch.setenv('PORTSHIELD_DEMO_TOKEN',TOKEN)
    monkeypatch.setenv('MODEL_BACKEND','baseline')
    with TestClient(app) as c:
        yield c

def test_api_auth_and_contract_limits(client):
    assert client.get('/healthz').status_code==200
    assert client.get('/readyz').status_code==200
    assert client.get('/metrics').status_code==401
    assert client.post('/v1/events/analyze',json={'text':'normal'}).status_code==401
    assert client.post('/v1/events/analyze',headers={'Authorization':'Bearer wrong'},json={'text':'normal'}).status_code==401
    headers={'Authorization':'Bearer '+TOKEN}
    r=client.post('/v1/events/analyze',headers=headers,json={'text':'Normal operations. No equipment failure.'})
    assert r.status_code==200 and r.json()['human_review_required'] is True
    assert client.post('/v1/events/analyze',headers=headers,json={'text':'x'*6001}).status_code==422
    assert client.post('/v1/rag/query',headers=headers,json={'question':'public data opening plan','roles':['admin']}).status_code==422
    assert not client.post('/v1/rag/query',headers=headers,json={'question':'public data opening plan'}).json()['abstained']

def test_jwt_signature_audience_expiry_and_roles(monkeypatch):
    monkeypatch.setenv('AUTH_MODE','jwt');monkeypatch.setenv('OIDC_ISSUER','https://internal.example/realm');monkeypatch.setenv('OIDC_AUDIENCE','portshield');monkeypatch.setenv('OIDC_JWKS_URL','https://internal.example/jwks')
    key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    monkeypatch.setattr(auth,'jwks',lambda url: SimpleNamespace(get_signing_key_from_jwt=lambda token:SimpleNamespace(key=key.public_key())))
    claims={'iss':'https://internal.example/realm','aud':'portshield','iat':int(time.time()),'exp':int(time.time())+300,'sub':'synthetic-analyst','realm_access':{'roles':['portshield-analyst']}}
    def request(payload,signing_key=key):
        token=jwt.encode(payload,signing_key,algorithm='RS256')
        with TestClient(app) as c:
            return c.get('/metrics',headers={'Authorization':'Bearer '+token})
    assert request(claims).status_code==200
    assert request({**claims,'aud':'another'}).status_code==401
    assert request({**claims,'exp':int(time.time())-10}).status_code==401
    assert request({**claims,'realm_access':{'roles':[]}}).status_code==403
    assert request(claims,rsa.generate_private_key(public_exponent=65537,key_size=2048)).status_code==401

def test_invalid_model_output_abstains_and_upstream_fails(client):
    class Invalid:
        def predict(self,text):return 'invalid JSON'
    original=app.state.client
    app.state.client=Invalid()
    headers={'Authorization':'Bearer '+TOKEN}
    assert client.post('/v1/events/analyze',headers=headers,json={'text':'Normal operations.'}).json()['event_type']=='unknown'
    class Offline:
        def predict(self,text):raise RuntimeError('internal failure')
    app.state.client=Offline()
    assert client.post('/v1/events/analyze',headers=headers,json={'text':'Normal operations.'}).status_code==503
    app.state.client=original
