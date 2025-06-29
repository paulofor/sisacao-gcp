## Prompt inicial para o OpenAI Codex / GPT-4o

```text
Você é o OpenAI Codex. Gere o código completo para app/main.py do projeto “stock-collector”.

Requisitos:

1. Runtime: Python 3.12 para Cloud Run Job (sem Flask).
2. Dados:
   • Ler gs://cotacao-intraday/bovespa.csv
   • Baixar candles 1m via yfinance.async
3. Processamento:
   • Último close por ticker
   • JSON: {ticker, data, hora, valor, hora_atual, data_hora_atual}
4. Persistência: BigQuery Storage Write API
   Dataset: cotacao_intraday, Tabela: cotacao_bovespa
5. Resiliência: 3 tentativas, back-off exponencial, log INFO
6. Config via env vars
7. Dependências mínimas
8. Runtime < 60 s

Retorne apenas o conteúdo final de app/main.py.
```
