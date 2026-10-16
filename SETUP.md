# Setup — AI Intelligence Digest

## What it does

- Runs once daily (07:17 UTC) or manually in **Actions > Daily AI Intelligence Digest > Run workflow**.
- Fetches RSS/Atom feeds and the five latest GitHub releases for each configured repository.
- Stores deduplicated findings in `data/findings.sqlite` and selects recent findings.
- Optionally uses a **local open-weight Qwen 0.5B quantized model** with `llama-cpp-python` for a short thematic summary, while listing individual primary-source findings verbatim/extractively.
- Overwrites `README.md`, `digest/latest.md`, and `docs/index.html` at every run. The SQLite history persists.
- Sends the report as a plain-text email if SMTP credentials are supplied.
- Can deploy the HTML through GitHub Pages.

## Getting started

1. Create a new GitHub repository (public if you want to avoid private Actions-minute charges; don't store sensitive collection data in a public repository).
2. Upload **all** files, preserving `.github/workflows/` and `src/` folder structure. Set default branch to `main`.
3. Go to **Settings > Actions > General > Workflow permissions** and allow **Read and write permissions** for `GITHUB_TOKEN` (or use a scoped token if your policy forbids this). This lets the workflow commit results back to the repository.
4. Go to **Settings > Secrets and variables > Actions > Secrets** and add `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `DIGEST_TO`. For Gmail, typically `smtp.gmail.com`, port `465`, and an app password on an eligible Google account; use an approved SMTP provider otherwise. Do not commit credentials to files.
5. Go to **Settings > Pages > Build and deployment** and select **GitHub Actions** as the publishing source.
6. Open **Actions > Daily AI Intelligence Digest > Run workflow**. Review logs, `README.md`, and the Pages deployment. The HTML digest is generated in `docs/index.html` and deployed in the same daily workflow.
7. Optionally add repository variable `USE_LOCAL_LLM=0` to skip CPU model inference. Other optional variables: `HF_GGUF_REPO`, `HF_GGUF_FILE`.

## Customize sources

Edit `sources.yaml`. The `sources` list expects `name`, `category`, and a real RSS/Atom feed `url`. `github_repos` expects `org/repo` names. Some feeds can change their URLs, block automation, omit dates, or be paywalled; failing feeds are logged and skipped. Verify source status in the Actions logs. Do not scrape restricted/paywalled pages without permission. Use official feeds/APIs where possible.

## Local test

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
USE_LOCAL_LLM=0 python -m src.pipeline
```

For local LLM generation:

```bash
pip install llama-cpp-python==0.3.16
python -m src.pipeline
```

The first local model run downloads a GGUF model from Hugging Face (roughly hundreds of MB). The default local model is intentionally tiny for GitHub-hosted CPU runners: **do not expect frontier-level summarization quality**. Read source-linked findings for accuracy. If model download, dependency compilation, or inference fails, the core report is still produced with source excerpts and links.

## Reliability and limits

- `schedule` runs only from GitHub's default branch. Scheduled jobs may be delayed or occasionally dropped; use Actions logs and workflow notifications to monitor failures. Public repository schedules may be disabled after 60 days of inactivity (daily bot commits are activity but GitHub policies can change).
- Free Actions usage depends on repository visibility and GitHub account limits. LLM installation and model downloads can consume runtime and bandwidth.
- The script tracks *newly published or updated items*, not all historical web content. It currently uses a rolling 36-hour window to tolerate missed runs and can repeat items on adjacent digests. It retains history for investigation.
- The digest **replaces the prior digest** but the repository's Git history still stores previous versions. SQLite history is committed to the repository, so don't make it public if findings contain private information.
- Pages is deployed in the same workflow because pushes made with the workflow `GITHUB_TOKEN` do not normally trigger separate push workflows.
- Email is plain text by design, reducing HTML formatting and security risks.
- Review daily log warnings when RSS URLs are invalid. The source catalog is a starter set, not a promise that every provider offers an active feed.
- The local LLM reads headline/excerpt text from untrusted sources; it is explicitly instructed to ignore instructions embedded in articles. No source text is executed.

## Architecture and upgrades

Next steps: scheduled hourly ingest + single daily digest; independent LLM scoring and citations; near-duplicate clustering; full article extraction where permitted; source-health metrics; evaluation runs; much larger catalog; language translation; personalized sections; actual article discovery via arXiv and publisher APIs; switch from SQLite to PostgreSQL when the repository database becomes too large or concurrent ingestion is needed.

## Full source-coverage edition

The full edition adds `extra_sources.yaml`, selective arXiv API searches, per-source health persistence (`source_health`), conservative near-duplicate headline clusters (`clusters`), and optional public-HTML enrichment (`enrichments`). The original `sources.yaml` still works. Expand these YAML source lists for additional regions, publishers, and topics. URLs in the extra catalog are **candidates**, not guaranteed live feeds. Inspect `digest/source-health.md` after the first run and fix or remove failed entries. Some publishers block feed requests and may require official API credentials.

Set GitHub Actions variable `USE_LOCAL_LLM=0` to make deployments fast and reliable without running an LLM. Keep `USE_LOCAL_LLM=1` for optional Qwen CPU synthesis. The extraction pipeline and links never depend on the LLM. Set `FETCH_FULL_TEXT=1` only if you want to attempt constrained, publicly available article text extraction (no login or paywall bypass). Enrichment is stored but the digest is intentionally composed from linked metadata and excerpts, not unrestricted text to prevent context and licensing problems.

**Reliability limits:** the collector records unsuccessful optional feeds and proceeds. GitHub Actions schedule can be delayed; use manual dispatch if needed. Public repositories expose their SQLite history and output: **do not include private data or secret feeds**. GitHub-hosted jobs are temporary, and committing SQLite into Git is only appropriate for modest datasets; move to a managed PostgreSQL database or object storage once history grows. SQLite binary pushes can occasionally conflict if humans also push while the workflow is running. SMTP credentials belong exclusively in Actions secrets. Read your mail provider's app-password / SMTP instructions.

**Current deployment target:** the report is rewritten in `README.md`, `digest/latest.md`, and `docs/index.html` each run; the dataset remains in `data/findings.sqlite`. GitHub Pages serves the current report. A separate source-health summary is written to `digest/source-health.md` and `docs/source-health.md`. Use a scheduled monthly cleanup or external database for indefinite retention.
