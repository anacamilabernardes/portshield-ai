# Publish from a clean archive

The downloadable archive excludes local Git history, dependencies, model weights and generated
experiment directories. Extract it and open the `portshield-ai` directory. Review the included
`repository-manifest.json` and run the publication guardrails before the first commit.

```bash
python scripts/check_publication.py
git init
git add .
git commit -m "Initial PortShield AI public-synthetic research reference"
git branch -M main
```

Create the repository under your own GitHub account and follow GitHub's displayed remote instructions.
Keep the MIT license and disclaimer. Enable private vulnerability reporting and branch protection,
and require the CPU CI checks. Do not store institutional credentials in CI. GPU runs belong on
reviewed controlled infrastructure with public/synthetic evaluation inputs.

Before posting model-performance claims, complete the independent domain and GPU experiments and
update the model card with exact artifact hashes and measured results. The ZIP is source code and
documentation for a research reference, not a production-ready trained model distribution.
