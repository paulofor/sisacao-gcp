# stock-collector

Coleta de cotações de ações B3 em frequência de 1 minuto e gravação no BigQuery, otimizado para custos mínimos no Google Cloud (Cloud Run + Scheduler + Storage Write API).

## Como usar

1. Edite `app/main.py` (ou gere via OpenAI Codex usando o prompt em `docs/PROMPT.md`).
2. `git push` no branch principal → Cloud Build containeriza e faz deploy automático.
3. Agende o Cloud Scheduler:  
   ```
   gcloud scheduler jobs create http stock-5min              --schedule="*/5 * * * *"              --uri=$(gcloud run services describe stock-collector --region=us-central1 --gen2 --format='value(status.url)')              --oidc-service-account=collector-sa@$PROJECT_ID.iam.gserviceaccount.com
   ```

Consulte o README completo para detalhes de custos e limites.
