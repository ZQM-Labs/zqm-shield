#!/usr/bin/env python3
"""release.py - Package ZQM Shield release with SHA-256 manifest."""
import hashlib, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    files = []
    for root, dirs, names in os.walk(ROOT):
        for name in names:
            abs_path = os.path.join(root, name)
            rel = os.path.relpath(abs_path, ROOT).replace('\\', '/')
            if rel.startswith('release-') or rel.startswith('.git'):
                continue
            files.append((rel, sha(abs_path), os.path.getsize(abs_path)))
    files.sort()
    manifest = {
        'version': '1.0.0',
        'files': [{'path': p, 'sha256': s, 'bytes': b} for p, s, b in files],
    }
    out = os.path.join(ROOT, 'release-zqm-shield-1.0.0.manifest.json')
    with open(out, 'w') as f:
        json.dump(manifest, f, indent=2)
        f.write('\n')
    print('Wrote', out, 'with', len(files), 'entries')


if __name__ == '__main__':
    main()
