# zqm-shield

Windows fleet attestation, quarantine, packaging, and Authenticode signing toolkit.

## About

`zqm-shield` provides defensive attestation workflows for Windows endpoints: evidence collection, quarantine/packaging, release verification, and Authenticode signing. It is the primary shield-side toolchain for ZQM fleet attestation.

## Installation

```bash
pip install -e .
```

Requires Python 3.11+ on Windows. Authenticode signing requires code-signing certificate access.

## Usage

```bash
# Collect endpoint evidence
zqm-shield collect --endpoint .

# Quarantine and package evidence
zqm-shield quarantine pack --input ./evidence/ --output ./packages/

# Verify a release bundle
zqm-shield verify --package ./packages/release.zip

# Sign a deliverable
zqm-shield sign --file ./packages/report.json --cert "CN=Alex Zelenski"
```

## Features

- Endpoint attestation evidence collection
- Quarantine packaging with SHA256 provenance
- Release verification (ZQ signature checks, chain integrity)
- Detached Authenticode/CMS signing of deliverables
- Windows driver audit and code-signing validation
- OSQuery-backed fleet queries
- CI-validated with ruff/mypy

## CI

[![CI](https://github.com/ZQM-Labs/zqm-shield/actions/workflows/ci.yml/badge.svg)](https://github.com/ZQM-Labs/zqm-shield/actions)
[![Ruff](https://img.shields.io/badge/lint-ruff-blue)](https://github.com/astral-sh/ruff)
[![Mypy](https://img.shields.io/badge/typecheck-mypy-blue)](https://github.com/python/mypy)

## License

MIT — see LICENSE file.

## Contact

Alex Zelenski — zqmcomputing@gmail.com
Brand: ZQM Computing / ZQM-Labs
