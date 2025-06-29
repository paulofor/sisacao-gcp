"""Cloud Run Job that:
1. Reads ticker list from a CSV on GCS
2. Fetches 1‑minute candles with yfinance (async)
3. Streams rows to BigQuery via Storage Write API
This is a skeleton generated for further development with OpenAI Codex.
"""

# TODO: implement full logic per README / prompt
def main(request=None):
    return "Hello from stock‑collector skeleton"
