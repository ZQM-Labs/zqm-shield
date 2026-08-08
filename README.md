# zqm-shield

<<<<<<< HEAD
![CI](https://github.com/ZQM-Labs/zqm-shield/actions/workflows/ci.yml/badge.svg)
![Tests](https://github.com/ZQM-Labs/zqm-shield/actions/workflows/tests.yml/badge.svg)
![Ruff](https://img.shields.io/badge/lint-ruff-blue)
![Mypy](https://img.shields.io/badge/type--check-mypy-green)

Windows fleet attestation, quarantine, packaging, and Authenticode signing toolkit.
||||||| parent of b0d72df (chore: T2 commercial surface + lint fixes)
Windows fleet attestation, quarantine, packaging, and Authenticode signing toolkit.
=======
Lightweight Windows endpoint quarantine/classify/sign pipeline.
>>>>>>> b0d72df (chore: T2 commercial surface + lint fixes)

## About

`zqm-shield` provides the classification, quarantine, and detached-signature pipeline for ZQM endpoint attestation. It consumes `zqm-intel-platforms` for shared OSINT/CTI/SIEM/Windows-telemetry primitives.

## Installation

```bash
pip install -r requirements.txt
```

Requires Python 3.11+ on Windows.

## Usage

```powershell
# Classify evidence
python -m zqm_shield classify --input ./evidence/ --output ./classified/

# Quarantine flagged artifacts
python -m zqm_shield quarantine --input ./classified/ --output ./quarantined/

# Sign deliverables
python -m zqm_shield sign --input ./quarantined/ --output ./signed/
```

## Features

- Evidence classification and quarantine staging
- Detached signature on attestation artifacts
- JSON schema validation via jsonschema
- Rich console output for operator workflows
- Pytest-based test surface

## CI

[![CI](https://github.com/ZQM-Labs/zqm-shield/actions/workflows/ci.yml/badge.svg)](https://github.com/ZQM-Labs/zqm-shield/actions)

## Integration: zqm-intel-platforms

This repo integrates with `zqm-intel-platforms` for shared OSINT/CTI/SIEM/Windows-telemetry primitives.

## License

MIT — see LICENSE file.

## Contact

Alex Zelenski — zqmcomputing@gmail.com
Brand: ZQM Computing / ZQM-Labs
<<<<<<< HEAD

## Integration: zqm-intel-platforms

This repo integrates with the [zqm-intel-platforms](https://github.com/ZQM-Labs/zqm-intel-platforms) hub for fleet-wide attestation and orchestration.

## Related Repositories

- [ZQM-Labs/zqm-attestation-toolkit](https://github.com/ZQM-Labs/zqm-attestation-toolkit) — Windows attestation, BitLocker, TPM, DFIR
- [ZQM-Labs/zqm-security-policy](https://github.com/ZQM-Labs/zqm-security-policy) — CIS benchmarks and Windows hardening
- [ZQM-Labs/pqc-readiness-toolkit](https://github.com/ZQM-Labs/pqc-readiness-toolkit) — post-quantum cryptography readiness
- [ZQM-Labs/zqm-public-tools](https://github.com/ZQM-Labs/zqm-public-tools) — open-source Windows security utilities
||||||| parent of b0d72df (chore: T2 commercial surface + lint fixes)

## Integration: zqm-intel-platforms

This repo integrates with the [zqm-intel-platforms](https://github.com/ZQM-Labs/zqm-intel-platforms) hub for fleet-wide attestation and orchestration.
=======
>>>>>>> b0d72df (chore: T2 commercial surface + lint fixes)
