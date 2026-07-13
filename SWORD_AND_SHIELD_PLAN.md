# Sword and Shield — ZQM Computing Plan

## Defs
- **Shield** = outward attestation deliverable. Buyer-facing.
- **Sword** = internal-only lightweight active probe. Feeds Shield evidence pack. Never sold standalone.

## Product surface rule
Only ZQM Computing appears in buyer-facing code/docs/responses. Sword stays internal tooling; its findings appear only inside Shield output.

## Revenue mapping
- Shield = subscription/perpetual license product ($49–$399/mo, Enterprise custom, Foundation $2,499 one-time).
- Sword = no separate SKU. Treated as module/add-on inside Shield SKU.
- Fulfillment: `purchase` issue label → GitHub Action → release artifact + license ID + receipt email.

## Current state
- `zqm-shield` scaffold exists at `C:\Users\zqmco\Desktop\enhance-repos\zqm-shield\`
- Quarantine (`src/quarantine.ps1`), study (`src/study.py`), classify (`src/classify.py`), sign stub (`src/sign.py`), release manifest all present
- `release.py` verified: 8-file manifest, exit 0
- `omnimap_primes.py --commas` delivers 2196-row prime-scoped comma atlas
- `zqm-attestation-toolkit` live at GitHub as `ZQM-Labs/zqm-attestation-toolkit` with CI, SKU catalog, commercial docs

## Remaining work
1. Relocate fulfill bot from `.hermes/scratch/scripts/fulfill_bot.py` into `zqm-attestation-toolkit/scripts/fulfill_bot.py` and wire workflow `run:` path.
2. Add repo-local fulfillment workflow files to both `zqm-attestation-toolkit` and `zqm-shield`.
3. Harden `sign.py` with real CMS binding workflow for `CN=Alex Zelenski`.
4. Pre-flight public readiness: strip secrets, verify no CVG artifacts, enforce `zqmcomputing@gmail.com` contact everywhere.
5. Release pipeline: tag → rebuild `releases/zqm_attestation_release_package.zip` → attach to GitHub release → fulfill bot sends download + receipt.
