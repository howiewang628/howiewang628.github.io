"""Reads the Google Scholar citation count through SerpApi and writes scholar/citations.json.

Run by .github/workflows/update-scholar.yml. Uses only the Python standard library.
The file is rewritten only when a number changes, so most runs make no commit.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

OUT = "scholar/citations.json"
SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "DBxarZYAAAAJ")
KEY = os.environ.get("SERPAPI_KEY", "").strip()

if not KEY:
    # No failed run (and no failure e-mail) before the secret is added.
    print("::warning::SERPAPI_KEY is not set; citations not updated.")
    sys.exit(0)

query = urllib.parse.urlencode({"engine": "google_scholar_author", "author_id": SCHOLAR_ID, "hl": "en", "api_key": KEY})
with urllib.request.urlopen(f"https://serpapi.com/search.json?{query}", timeout=60) as response:
    data = json.load(response)

if "error" in data:
    sys.exit(f"SerpApi error: {data['error']}")

table = data["cited_by"]["table"]


def total(name):
    return next(int(row[name]["all"]) for row in table if name in row)


new = {"citations": total("citations"), "h_index": total("h_index"), "i10_index": total("i10_index")}

try:
    with open(OUT, encoding="utf-8") as f:
        old = json.load(f)
except (OSError, ValueError):
    old = {}

if all(old.get(k) == v for k, v in new.items()):
    print(f"Unchanged: {new}")
    sys.exit(0)

# Google Scholar totals rarely fall; a large drop is more likely a bad reply than real.
if old.get("citations") and new["citations"] < old["citations"] * 0.5:
    sys.exit(f"Refusing to save a large drop: {old['citations']} -> {new['citations']}")

new["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
new["profile"] = f"https://scholar.google.com/citations?user={SCHOLAR_ID}"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(new, f, indent=2)
    f.write("\n")
print(f"Saved: {new}")
