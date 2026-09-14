#!/usr/bin/env python3
"""Lightweight documentation preview server for the Nullaroni's Skyrim repo.

This repository is a documentation + Wabbajack modlist-configuration project,
not a conventional runnable application. This server renders the Markdown
specification files to HTML, shows the modlist cover image, and pretty-prints
(and validates) the Wabbajack compiler settings JSON so contributors can review
the docs and config in a browser.
"""

import html
import json
import os
import socketserver
from http.server import BaseHTTPRequestHandler

import markdown

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = "0.0.0.0"
PORT = int(os.environ.get("DOCS_PORT", "8080"))

MARKDOWN_PAGES = [
    ("README.md", "Overview"),
    ("baseline-inventory.md", "Baseline Inventory"),
    ("outline.md", "Specification"),
]
JSON_CONFIG = "NGVO.compiler_settings"
COVER_IMAGE = "Nullaronis.webp"

MD_EXTENSIONS = ["extra", "toc", "sane_lists", "nl2br"]

PAGE_STYLE = """
:root { color-scheme: dark; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #0d1117;
  color: #e6edf3;
  line-height: 1.6;
}
header {
  padding: 24px 32px;
  background: linear-gradient(120deg, #1b2233, #0d1117);
  border-bottom: 1px solid #30363d;
}
header h1 { margin: 0 0 4px; font-size: 22px; }
header p { margin: 0; color: #8b949e; font-size: 14px; }
.layout { display: flex; min-height: calc(100vh - 92px); }
nav {
  width: 240px;
  flex: 0 0 240px;
  border-right: 1px solid #30363d;
  padding: 20px 16px;
  background: #0f141b;
}
nav a {
  display: block;
  padding: 8px 12px;
  margin-bottom: 4px;
  border-radius: 6px;
  color: #adbac7;
  text-decoration: none;
  font-size: 14px;
}
nav a:hover { background: #1b2230; color: #fff; }
nav a.active { background: #1f6feb; color: #fff; }
main { flex: 1; padding: 32px 40px; max-width: 900px; }
main img { max-width: 100%; border-radius: 8px; }
pre {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  padding: 16px;
  overflow-x: auto;
}
code { background: #161b22; padding: 2px 6px; border-radius: 4px; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 16px 0; }
th, td { border: 1px solid #30363d; padding: 8px 12px; text-align: left; }
th { background: #161b22; }
h1, h2, h3 { border-bottom: 1px solid #21262d; padding-bottom: 6px; }
.badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
}
.badge.ok { background: #1a7f37; color: #fff; }
.badge.err { background: #a40e26; color: #fff; }
"""


def build_nav(active):
    links = []
    for path, label in MARKDOWN_PAGES:
        cls = "active" if path == active else ""
        links.append(f'<a class="{cls}" href="/{path}">{html.escape(label)}</a>')
    cls = "active" if active == JSON_CONFIG else ""
    links.append(f'<a class="{cls}" href="/config">Compiler Settings (JSON)</a>')
    cls = "active" if active == COVER_IMAGE else ""
    links.append(f'<a class="{cls}" href="/cover">Cover Image</a>')
    return "\n".join(links)


def render_shell(active, title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)} — Nullaroni's Skyrim</title>
  <style>{PAGE_STYLE}</style>
</head>
<body>
  <header>
    <h1>Nullaroni's Skyrim — Documentation Preview</h1>
    <p>Skyrim AE / NGVO expansion modlist specification and Wabbajack config</p>
  </header>
  <div class="layout">
    <nav>{build_nav(active)}</nav>
    <main>{body}</main>
  </div>
</body>
</html>"""


def render_markdown_page(path):
    with open(os.path.join(REPO_ROOT, path), "r", encoding="utf-8") as fh:
        text = fh.read()
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def render_config_page():
    config_path = os.path.join(REPO_ROOT, JSON_CONFIG)
    with open(config_path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    try:
        parsed = json.loads(raw)
        pretty = json.dumps(parsed, indent=2)
        badge = '<span class="badge ok">Valid JSON</span>'
        keys = len(parsed)
        summary = f"<p>{badge} &nbsp; {keys} top-level keys.</p>"
    except json.JSONDecodeError as exc:
        pretty = raw
        badge = '<span class="badge err">Invalid JSON</span>'
        summary = f"<p>{badge} &nbsp; {html.escape(str(exc))}</p>"
    return (
        f"<h1>{JSON_CONFIG}</h1>{summary}"
        f"<pre><code>{html.escape(pretty)}</code></pre>"
    )


def render_cover_page():
    return (
        f"<h1>Modlist Cover Image</h1>"
        f'<p><code>{COVER_IMAGE}</code> (1600x900 WebP)</p>'
        f'<img src="/{COVER_IMAGE}" alt="Nullaroni\'s Skyrim cover art" />'
    )


class DocsHandler(BaseHTTPRequestHandler):
    def _send(self, status, body, content_type="text/html; charset=utf-8"):
        payload = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        route = self.path.split("?", 1)[0].rstrip("/") or "/"

        if route == "/":
            self._send(200, render_shell(
                "README.md", "Overview", render_markdown_page("README.md")))
            return

        if route == "/config":
            self._send(200, render_shell(
                JSON_CONFIG, "Compiler Settings", render_config_page()))
            return

        if route == "/cover":
            self._send(200, render_shell(
                COVER_IMAGE, "Cover Image", render_cover_page()))
            return

        if route == f"/{COVER_IMAGE}":
            image_path = os.path.join(REPO_ROOT, COVER_IMAGE)
            if os.path.exists(image_path):
                with open(image_path, "rb") as fh:
                    self._send(200, fh.read(), "image/webp")
                return

        for path, label in MARKDOWN_PAGES:
            if route == f"/{path}":
                self._send(200, render_shell(
                    path, label, render_markdown_page(path)))
                return

        self._send(404, render_shell("", "Not Found", "<h1>404</h1>"))

    def log_message(self, fmt, *args):
        print("[docs-preview] " + (fmt % args))


def main():
    with socketserver.ThreadingTCPServer((HOST, PORT), DocsHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"[docs-preview] Serving documentation on http://{HOST}:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
