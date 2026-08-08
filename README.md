# zqm-shield

## Purpose
Quarantine/classify pipeline for isolated artifact handling.

## What it does
- Copies artifacts to quarantine with preserved SHA-256 (`src/quarantine.py`)
- Builds evidence pack (`src/study.py`)
- Classifies artifacts (`src/classify.py`)
- Signs evidence with Authenticode (`src/sign.py`)

## Integration: zqm-intel-platforms
zqm-shield is a PowerShell-first repo. It does not vendor `zqm-intel-platforms`
into its runtime build surface; instead, use the wrapper at
`examples/intel_wrapper_example.md` for cross-language export of quarantine
evidence to SIEM sinks defined by `zqm-intel-platforms`.

## Requirements
Use in PowerShell 5.1+ on Windows 10/11. Review the included scripts before importing or running them.

## Contact
ZQM Computing — zqmcomputing@gmail.com

## Support
Development is funded commercially — see the toolkit's [FUNDING](https://github.com/ZQM-Labs/zqm-attestation-toolkit/blob/main/.github/FUNDING.yml) for sponsorship, procurement, and no-KYC options. You can also [sponsor ZQM-Computing on GitHub](https://github.com/sponsors/ZQM-Computing).

## Commercial Licensing & Procurement
This repository is free for personal and audit use under its stated license. Enterprise procurement, retainers, and add-on tiers are available:

- Pricing & SKUs: [COMMERCIAL.md](COMMERCIAL.md) · [SKU_CATALOG.md](SKU_CATALOG.md)
- Start a purchase: open a [Purchase request](https://github.com/ZQM-Labs/zqm-shield/issues/new?template=purchase_request.yml) issue
- Contact: zqmcomputing@gmail.com

All deliverables are CMS-signed and independently verifiable.

## License
See repo license file. No AGPL/AGPL/BSL/CPAL on brand surface.
