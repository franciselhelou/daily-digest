# AI Intelligence Digest — full starter implementation

Daily scheduled, source-linked AI intelligence collector for GitHub Actions.

## Components
- `sources.yaml`: baseline RSS feeds and GitHub release monitoring
- `extra_sources.yaml`: expanded categorized feed candidates and targeted arXiv searches
- `src/pipeline.py`: core SQLite ingestion, candidate selection, optional LLM digest, email, Pages
- `src/advanced.py`: source-health tracking, auxiliary feeds, arXiv searches, optional public-page extraction, headline clustering
- `digest/latest.md`: overwritten on each run; `data/findings.sqlite`: historical observations
- `digest/source-health.md`: which expanded endpoints failed or succeeded
- `.github/workflows/daily.yml`: scheduled job and Pages publishing
- `SETUP.md`: GitHub setup, secrets and architecture caveats

## Commands
```
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
USE_LOCAL_LLM=0 python -m src.pipeline
```

GitHub-hosted runners require no paid LLM API when using `USE_LOCAL_LLM=0`; optional Qwen local inference uses `llama-cpp-python`, which can be costly to install/execute. Many of the source URLs are discovery candidates that require monitoring: never mistake failures for a guarantee that publishers stopped publishing. This prototype performs conservative lexical duplicate clustering, not embedding-semantic clustering. For multi-year intelligence collection, plan a remote database and periodic historical summarization.
