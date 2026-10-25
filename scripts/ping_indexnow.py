#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, Naver, Seznam, Yep) with all site URLs after a deploy.
Google does not use IndexNow - Google relies on sitemaps + Search Console.
Non-fatal: a failed ping never fails the workflow."""
import json, sys, os, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_lib import INDEXNOW_KEY, SITE, SECTIONS

urls = [SITE + "/"] + [f"{SITE}/{s[0]}.html" for s in SECTIONS]
payload = {
    "host": "ranakhan77.github.io",
    "key": INDEXNOW_KEY,
    "keyLocation": f"{SITE}/{INDEXNOW_KEY}.txt",
    "urlList": urls,
}
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"})
try:
    resp = urllib.request.urlopen(req, timeout=30)
    print("IndexNow response:", resp.status, "(200=OK, 202=accepted for processing)")
except Exception as e:
    print("IndexNow ping failed (non-fatal):", e)
