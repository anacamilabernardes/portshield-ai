import asyncio, json
import httpx
from portshield_ai.benchmark import benchmark, parse_sse

def test_streaming_usage_empty_role_and_throughput(monkeypatch,tmp_path):
    assert parse_sse('data: [DONE]') is None
    assert parse_sse('event: message') is None
    original=httpx.AsyncClient
    lines=[{'choices':[{'delta':{'role':'assistant'}}]}, {'choices':[{'delta':{'content':'{}'}}]}, {'choices':[],'usage':{'completion_tokens':2}}]
    def handler(request):
        return httpx.Response(200, text='\n'.join('data: '+json.dumps(x) for x in lines)+'\ndata: [DONE]\n')
    monkeypatch.setattr(httpx,'AsyncClient',lambda **kwargs:original(transport=httpx.MockTransport(handler),**kwargs))
    out=tmp_path/'bench.json'
    result=asyncio.run(benchmark('http://localhost/v1','portshield',['a','b'],out,concurrency=2,warmup=1))
    assert result['requests']==2
    assert result['ttft_seconds']['n']==2
    assert result['completion_tokens_per_second']>0
    assert result['peak_server_gpu_memory_mib'] is None
