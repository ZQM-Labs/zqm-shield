# zqm-shield

![CI](https://github.com/ZQM-Labs/zqm-shield/actions/workflows/ci.yml/badge.svg)
![Tests](https://github.com/ZQM-Labs/zqm-shield/actions/workflows/tests.yml/badge.svg)
![Ruff](https://img.shields.io/badge/lint-ruff-blue)
![Mypy](https://img.shields.io/badge/type--check-mypy-green)

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

## Integration: zqm-intel-platforms

This repo integrates with the [zqm-intel-platforms](https://github.com/ZQM-Labs/zqm-intel-platforms) hub for fleet-wide attestation and orchestration.

## Related Repositories

- [ZQM-Labs/zqm-attestation-toolkit](https://github.com/ZQM-Labs/zqm-attestation-toolkit) — Windows attestation, BitLocker, TPM, DFIR
- [ZQM-Labs/zqm-security-policy](https://github.com/ZQM-Labs/zqm-security-policy) — CIS benchmarks and Windows hardening
- [ZQM-Labs/pqc-readiness-toolkit](https://github.com/ZQM-Labs/pqc-readiness-toolkit) — post-quantum cryptography readiness
- [ZQM-Labs/zqm-public-tools](https://github.com/ZQM-Labs/zqm-public-tools) — open-source Windows security utilities
