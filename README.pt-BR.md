# PortShield AI

**Plataforma Soberana de Inteligência para Resiliência da Infraestrutura Portuária e Logística**

Protótipo independente de apoio à análise humana da continuidade portuária e logística. A arquitetura proposta prevê execução local no data center do MPOR, fine-tuning de pequenos modelos de linguagem, RAG privado e componentes quantitativos de forecasting e análise de grafos. O projeto não declara aprovação, patrocínio ou implantação pelo Ministério.

O código disponível demonstra classificação por regras, recuperação local de evidências com filtro de acesso, previsão por média móvel, cenários de conectividade e registro de revisão humana. Todos os dados são sintéticos. SLM, fine-tuning e RAG generativo são etapas futuras, descritas na documentação em inglês.

```sh
python -m portshield demo --output artifacts
python -m unittest discover -s tests -v
```

Requer Python 3.11 ou superior. Não exige chave de API, GPU ou acesso à internet. O relatório fica em `artifacts/report.json`. Consulte o [README principal](README.md) para funcionamento, limitações e arquitetura.
