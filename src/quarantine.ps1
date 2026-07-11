<#
.SYNOPSIS
ZQM Shield - Quarantine module.
.PARAMETER Source
Path to evidence or artifact to quarantine.
.PARAMETER QuarantineDir
Destination quarantine root.
.EXAMPLE
powershell -ExecutionPolicy Bypass -File src/quarantine.ps1 -Source C:\temp\artifact -QuarantineDir C:\quarantine
#>
param(
  [Parameter(Mandatory)] [string] $Source,
  [Parameter(Mandatory)] [string] $QuarantineDir
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $Source)) {
  Write-Error "Source not found: $Source"
  exit 1
}

$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$dest = Join-Path $QuarantineDir ("q-" + $stamp)
New-Item -ItemType Directory -Path $dest -Force | Out-Null

$hashPath = Join-Path $dest 'source.sha256'
$stream = [System.IO.File]::Open($Source, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::Read)
$sha256 = [System.Security.Cryptography.SHA256]::Create()
$computed = $sha256.ComputeHash($stream)
[Array]::Reverse($computed)
$hex = [BitConverter]::ToString($computed).Replace('-', '').ToLowerInvariant()
$stream.Close()
Set-Content -LiteralPath $hashPath -Value $hex -NoNewline

$dst = Join-Path $dest (Split-Path -Leaf $Source)
if ((Get-Item -LiteralPath $Source).PSIsContainer) {
  Copy-Item -LiteralPath $Source -Destination $dst -Recurse -Force
} else {
  Copy-Item -LiteralPath $Source -Destination $dst -Force
}

Write-Output (Join-Path $dest 'manifest.ps1')
