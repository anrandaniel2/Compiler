import base64
import json
import os
import sys

BUNDLE_FILE = "source_bundle.txt"

if not os.path.exists(BUNDLE_FILE):
    print("No bundle file found, skipping extraction.")
    sys.exit(0)

print("Extracting source bundle...")

with open(BUNDLE_FILE, "r") as f:
    encoded = f.read().strip()

decoded = base64.b64decode(encoded).decode("utf-8")
files = json.loads(decoded)

count = 0
for filepath, content in files.items():
    dir_path = os.path.dirname(filepath)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)
    count += 1

print("Extracted " + str(count) + " files!")
os.remove(BUNDLE_FILE)
print("Bundle cleanup done.")
