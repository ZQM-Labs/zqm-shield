#!/usr/bin/env python3
"""src/sign.py - CMS/Authenticode sign evidence artifacts on Windows.

Uses the first code-signing certificate found in the current-user personal
store.  No ZQM-specific CN, paths, or hostnames are hardcoded here.
"""
import os
import subprocess
import sys


PS_TPL = """
$ErrorActionPreference = 'Stop'
$store = 'Cert:\\CurrentUser\\My'
$cert = Get-ChildItem $store -CodeSigningCert | Select-Object -First 1
if (-not $cert) { throw 'No code-signing certificate found in CurrentUser\\My.' }

$files = @(%s)
if (-not $files) { throw 'No files provided.' }

foreach ($f in $files) {
  $pair = New-Object System.Management.Automation.PSObject -Property @{Path=$f; Status='OK'}
  try {
    $sig = Set-AuthenticodeSignature -FilePath $f -Certificate $cert -HashAlgorithm SHA256
    $pair.Status = ('Signed: Status={0}, StatusString={1}'.format($sig.Status, $sig.StatusString))
  } catch {
    $pair.Status = ('ERROR: {0}'.format($_))
  }
  $pair | ConvertTo-Json -Compress
}
"""


def main():
    if len(sys.argv) < 2:
        print('Usage: sign.py <artifact_dir> [file1 file2 ...]')
        sys.exit(2)

    artifact_dir = sys.argv[1]
    extra = sys.argv[2:]

    if not os.path.isdir(artifact_dir):
        print('Not a directory:', artifact_dir)
        sys.exit(2)

    candidates = ['manifest.json', 'classification.json'] + extra
    files = [os.path.join(artifact_dir, c) for c in candidates if os.path.exists(os.path.join(artifact_dir, c))]

    if not files:
        print('No signable files found in', artifact_dir)
        sys.exit(2)

    ps_args = ','.join('"' + f.replace('"', '`"') + '"' for f in files)
    ps = PowerShell(PS_TPL % ps_args)
    out = ps.run()
    print(out)


class PowerShell:
    def __init__(self, script: str):
        self.script = script

    def run(self) -> str:
        cmd = [
            'powershell',
            '-NoLogo',
            '-NoProfile',
            '-NonInteractive',
            '-ExecutionPolicy', 'Bypass',
            '-Command', self.script,
        ]
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return p.stdout.strip()
        except subprocess.CalledProcessError as e:
            return 'ERROR: ' + (e.stderr or e.stdout or str(e))


if __name__ == '__main__':
    main()
