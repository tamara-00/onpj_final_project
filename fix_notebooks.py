import json
import glob
import sys
import os

# Usage: python fix_notebooks.py          <- fixes all .ipynb in current folder
#        python fix_notebooks.py /path/   <- fixes all .ipynb in given folder

folder = sys.argv[1] if len(sys.argv) > 1 else '.'
notebooks = glob.glob(os.path.join(folder, '**', '*.ipynb'), recursive=True)

if not notebooks:
    print("No .ipynb files found.")
else:
    for path in notebooks:
        with open(path) as f:
            nb = json.load(f)
        if 'widgets' in nb.get('metadata', {}):
            del nb['metadata']['widgets']
            with open(path, 'w') as f:
                json.dump(nb, f, indent=2)
            print(f"✅ Fixed: {path}")
        else:
            print(f"⏭️  Skipped (no widgets): {path}")

print("\nDone!")
