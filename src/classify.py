#!/usr/bin/env python3
"""src/classify.py - Classify quarantined artifact as benign, suspicious, malicious."""
import json, os, sys

def main():
    if len(sys.argv) < 2:
        print('Usage: classify.py <quarantine_dir>'); sys.exit(2)
    qdir = sys.argv[1]
    manifest_path = os.path.join(qdir, 'manifest.json')
    if not os.path.exists(manifest_path):
        print('Missing evidence. Run study.py first.'); sys.exit(2)
    with open(manifest_path) as f:
        ev = json.load(f)
    file_count = len(ev.get('files', []))
    total_bytes = sum(item.get('bytes', 0) for item in ev.get('files', []))
    classification = 'suspicious'
    if file_count == 0 or total_bytes == 0:
        classification = 'benign'
    ev['classification'] = classification
    ev['classified_at'] = __import__('datetime').datetime.utcnow().isoformat() + 'Z'
    ev['classification_notes'] = (
      'Automated heuristic: empty or zero-byte artifacts classified benign; '
      'non-empty preserved artifacts classified suspicious.'
    )
    print('Classified as:', classification)
    out = os.path.join(qdir, 'classification.json')
    with open(out, 'w') as f:
      json.dump(ev, f, indent=2)
      f.write('\n')
    print('Output:', out)

if __name__ == '__main__':
    main()
