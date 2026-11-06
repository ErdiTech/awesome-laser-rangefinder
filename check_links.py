import re, sys, urllib.request
links = re.findall(r"\]\((https?://[^)]+)\)", open("README.md", encoding="utf-8").read())
bad = []
for u in links:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 awesome-link-check"})
        code = urllib.request.urlopen(req, timeout=20).getcode()
    except Exception as e:
        code = getattr(e, "code", str(e))
    print(code, u)
    if code not in (200, 301, 302, 403, 429): bad.append(u)
print(f"{len(links)} links, {len(bad)} failing")
sys.exit(1 if bad else 0)
