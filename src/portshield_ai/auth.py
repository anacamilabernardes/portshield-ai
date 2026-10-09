import os
import secrets
from functools import lru_cache
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

bearer = HTTPBearer(auto_error=False)
@lru_cache
def jwks(url):
    import jwt
    return jwt.PyJWKClient(url, cache_keys=True, lifespan=300, timeout=5)

def principal(credentials: HTTPAuthorizationCredentials | None = Depends(bearer)):
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(401, "Authentication required")
    mode = os.getenv("AUTH_MODE", "jwt")
    if mode == "demo":
        expected = os.getenv("PORTSHIELD_DEMO_TOKEN", "")
        if len(expected) < 24 or not secrets.compare_digest(credentials.credentials, expected):
            raise HTTPException(401, "Invalid credentials or demo configuration")
        return {"sub": "demo-user", "roles": ["analyst"], "assurance": "shared_demo_token"}
    if mode != "jwt":
        raise HTTPException(503, "Authentication misconfigured")
    try:
        import jwt
        issuer, audience, url = [os.environ[k] for k in ("OIDC_ISSUER", "OIDC_AUDIENCE", "OIDC_JWKS_URL")]
        key = jwks(url).get_signing_key_from_jwt(credentials.credentials).key
        claims = jwt.decode(credentials.credentials, key, algorithms=["RS256"], issuer=issuer, audience=audience,
            options={"require": ["exp", "iat", "sub", "iss", "aud"]})
        roles = claims.get("realm_access", {}).get("roles", [])
        if "portshield-analyst" not in roles:
            raise HTTPException(403, "Analyst role required")
        return {"sub": claims["sub"], "roles": ["analyst"], "assurance": "signed_jwt"}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(401, "Invalid credentials") from None
