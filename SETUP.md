# Daily AI Intelligence Dashboard — V3 Setup

## What's new

- Exactly 24 rolling hours, **based on published timestamps**, no future-dated or undated articles.
- 10 ranked top events rather than hundreds of stories in the email and README.
- Category tabs, score counts, search, priority filter, and expandable complete per-category coverage in GitHub Pages.
- One canonical event per near-duplicate headline, with links to alternative sources.
- Per-source health diagnostics, including failed feeds and GitHub repositories.
- Optional CPU-based Qwen GGUF synthesis for executive and category commentary. When disabled/unavailable the dashboard transparently uses deterministic evidence excerpts, **not AI-generated summaries**.

## Install / Upgrade

1. Unzip the project and upload **its contents** into the root of your existing GitHub repository, replacing matching files. Retain your `data/findings.sqlite` from the existing repository if you need history; the ZIP has no database and does not overwrite it.
2. Commit the modified `.github/workflows/daily.yml`, `src/` files, `sources.yaml`, `extra_sources.yaml`, `tests/`, and `SETUP.md`.
3. Actions → **Daily AI Intelligence Digest** → **Run workflow**. Wait for collection and publishing.
4. GitHub Pages site: `https://YOUR_USERNAME.github.io/YOUR_REPOSITORY/`. GitHub Pages must be enabled, and public visibility may be necessary depending on plan.
5. See `docs/index.html`, `docs/data.json`, `docs/app.js`, and `docs/style.css` in the generated commit.

## Configuration

- **Window is fixed to the preceding 24 hours**; cannot be extended via environment accidentally.
- `TOP_STORIES` (optional, defaults 10): top story count in executive overview.
- `MAX_PER_SOURCE` (default 35): maximum entries fetched per feed before strict filtering. To increase coverage for very busy sources, use 100.
- `ENABLE_ARXIV_SEARCH` (default 1): targeted arXiv API collection.
- `USE_LOCAL_LLM` repository **variable**: `1` (default) enables optional llama.cpp CPU model; `0` gives reliable, clearly labeled deterministic summaries. On GitHub Actions a C++ build or model download may fail or time out; local inference cannot be guaranteed within runner resources.
- `HF_GGUF_REPO`, `HF_GGUF_FILE`, `GGUF_PATH` optional model selection.
- SMTP secrets: `SMTP_HOST`, `SMTP_PORT` (465 SSL or 587 STARTTLS), `SMTP_USER`, `SMTP_PASSWORD`, `DIGEST_TO`.

## Source problems from the sample run

The supplied run contained: 401 (Hugging Face Papers RSS), 403 (The Batch and Import AI), 404 (invalid or moved URLs), 429 (VentureBeat and Reddit), and a timeout (Hacker News). Such sources are **disabled in YAML**, with `enabled: false`, not deleted. Their publishers remain legitimate, but these exact endpoints were not reliable in your runner. Reactivate one at a time only after finding a working, permitted endpoint. For relevant materials without RSS, prefer publishers' APIs or email newsletters rather than scraping restricted sites. The broken `aider-chat/aider` repository has been changed to `Aider-AI/aider` (verify its availability on your next run).

## Data and ranking caveats

Events are grouped by lexical headline similarity, not true semantic similarity; it can both miss duplicates and combine very similar stories. Scores are **heuristics** based on topical interest terms, release/importance signals, and source type. A label such as High signal means *candidate to examine*, not a factually established breakthrough. Research preprints remain unverified. No ranking model can know the true significance from an abstract alone.

Previously stored history is retained. The 24h display includes only `published` dates in window, not 'newly inserted' dates. Reports overwrite `README.md`, `digest/latest.md`, and `docs/index.html` + `docs/data.json` each run, while the SQLite database persists.

## Tests

`python -m pip install -r requirements.txt` then `python -m unittest discover -s tests -v`.

For an email-only private-repo setup, remove or conditionally disable the GitHub Pages deployment steps. The collection and digest can run without Pages.

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

## Add sources directly from the dashboard (V3.1)

The dashboard has an **Add a new intelligence source** field. Paste a full HTTPS RSS/Atom feed URL, select a category, and click **Add source**.

The button opens a prefilled GitHub issue. **Click Submit new issue on GitHub** to confirm your request. This extra confirmation is required because GitHub Pages is static and cannot safely write to the repository without authenticated server-side code.

The `.github/workflows/add-source.yml` workflow accepts these requests **only from the repository owner**, checks the URL and category, prevents duplicate URL entries, and updates `extra_sources.yaml`. It comments on and closes a successfully processed issue. The new source starts collecting at the following daily run. Failed requests remain open and the Action log explains why.

**Required settings:** GitHub **Settings → General → Features → Issues** must be enabled; in **Settings → Actions → General**, Workflow permissions must permit the Actions token to write to repository contents. Keep the `add-source.yml` workflow on the default branch. If you rename or transfer the repository, update `const repo='franciselhelou/daily-digest'` in `src/dashboard.py` and re-run the daily workflow to regenerate the dashboard. You can restrict Issue submissions to the owner via the workflow authorization guard; untrusted users cannot write source files through this workflow.

**Source behavior:** RSS or Atom URLs are the reliable option. A generic website URL can be registered but may not yield any items until a suitable feed endpoint or a site-specific ingestion adapter is provided. Be sure to check the source-health section after the following run.

The source submission form is generated as part of `docs/index.html` at the next successful daily digest run. Do not manually paste access tokens into the webpage.
