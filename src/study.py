#!/usr/bin/env python3
"""src/study.py - Build evidence pack with who/what/where/why + hash manifest."""
import hashlib, json, os, sys, datetime

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def main():
    if len(sys.argv) < 2:
        print('Usage: study.py <quarantine_dir>'); sys.exit(2)
    qdir = sys.argv[1]
    manifest_path = os.path.join(qdir, 'manifest.json')
    if os.path.exists(manifest_path):
        print('Evidence already studied:', manifest_path); return
    source_hash_path = os.path.join(qdir, 'source.sha256')
    source_sha = ''
    if os.path.exists(source_hash_path):
        with open(source_hash_path) as f:
            source_sha = f.read().strip()
    walk = []
    for root, dirs, files in os.walk(qdir):
        for name in files:
            path = os.path.join(root, name)
            rel = os.path.relpath(path, qdir)
            walk.append({'path': rel.replace('\\', '/'), 'sha256': sha(path), 'bytes': os.path.getsize(path)})
    evidence = {
      'schema': 'zqm-shield/evidence/1',
      'quarantine_dir': qdir,
      'source_sha256': source_sha,
      'who': 'ZQM Shield automated quarantine',
      'what': 'copied artifact; source hash preserved under source.sha256',
      'where': qdir,
      'why': 'incident triage: isolate for study and classification',
      'collected_at': datetime.datetime.utcnow().isoformat() + 'Z',
      'files': walk
    }
    out = os.path.join(qdir, 'manifest.json')
    with open(out, 'w') as f:
      json.dump(evidence, f, indent=2)
      f.write('\n')
    print('Evidence:', out)

if __name__ == '__main__':
    main()
