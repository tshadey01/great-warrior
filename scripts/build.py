#!/usr/bin/env python3
"""Build the GitHub Pages site from the project's HTML sources.

The sources are page fragments (no <!doctype>/<head>), so each one is wrapped
in a full document here.

Usage: python3 scripts/build.py [GIG_RUN_HTML] [SOUND_LAB_HTML]
Defaults point at the project's shared folder.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = {
    "index.html": sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/gig-run/great-warrior-gig-run.html",
    "sound-lab/index.html": sys.argv[2] if len(sys.argv) > 2 else "/mnt/project-files/sound-lab/sound-lab.html",
}
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
"""

for out, src in SRC.items():
    body = pathlib.Path(src).read_text(encoding="utf-8")
    if body.lstrip().lower().startswith("<!doctype"):
        html = body
    else:
        html = HEAD + body + "\n</html>\n"
    dest = ROOT / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({len(html)//1024} KB) from {src}")
