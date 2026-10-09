# PortShield AI — Resiliência Soberana da Infraestrutura Marítima Crítica

Projeto independente de Engineering Manager / Applied AI Lead. Demonstra classificação e extração
estruturada de eventos, abstenção, especialização de SLM por LoRA/QLoRA, quantização NF4,
serving privado com vLLM, FastAPI, RAG local e avaliação reproduzível.

Somente dados públicos e sintéticos. Não inclui o PDF institucional, incidentes reais, topologias,
credenciais, dados pessoais ou informação sensível do MPOR. Não representa produto oficial ou aprovado.
Todo resultado exige revisão humana; nenhum comando operacional é executado.

O [README técnico](README.md) contém todos os comandos e a distinção entre código entregue,
verificação em CPU e etapas dependentes de GPU. Os seis notebooks percorrem exploração, baseline,
fine-tuning, quantização, benchmark e RAG. Resultados de GPU permanecem não medidos.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,toy]"
portshield-ai generate
portshield-ai evaluate
python -m pytest -q
$env:AUTH_MODE="demo"
$env:PORTSHIELD_DEMO_TOKEN = python -c "import secrets; print(secrets.token_urlsafe(32))"
uvicorn portshield_ai.api:app --host 127.0.0.1 --port 8000
```

O PIDP orienta os princípios gerais de plataforma compartilhada, open source por padrão,
soberania informacional, Bronze–Silver–Gold, responsáveis por dados, IAM e MLOps.
O [mapa de alinhamento](docs/pidp-alignment.md) relaciona esses princípios aos componentes.
A licença MIT aplica-se ao conteúdo original. Modelos e fontes externas conservam suas licenças.
O experimento toy de SVD/MPO/Tensor Train não reproduz CompactifAI.
