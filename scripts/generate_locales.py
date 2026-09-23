#!/usr/bin/env python3
"""Build static localized legal pages from content/<locale>.json."""

import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = {path.stem: json.loads(path.read_text(encoding="utf-8")) for path in (ROOT / "content").glob("*.json")}
SECTIONS = ("privacy", "privacy-choices", "delete-account", "support")
EMAIL = "ytwl1013@gmail.com"
LOCALE_ORDER = ("en-us", "en-gb", "de", "fr", "zh-cn", "pt-pt", "es-es", "it", "nl", "pl")
LOCALE_NAMES = {
    "en-us": "English (US)", "en-gb": "English (UK)", "de": "Deutsch",
    "fr": "Français", "zh-cn": "简体中文", "pt-pt": "Português",
    "es-es": "Español", "it": "Italiano", "nl": "Nederlands", "pl": "Polski",
}


def page_url(section, locale):
    return f"../../{section}/" if locale == "en-us" else f"../../{section}/{locale}/"


def language_nav(section, selected):
    links = []
    for locale in LOCALE_ORDER:
        current = ' aria-current="page"' if locale == selected else ""
        links.append(f'<a{current} lang="{escape(CONTENT[locale]["lang"])}" href="{page_url(section, locale)}">{escape(LOCALE_NAMES[locale])}</a>')
    return '<nav class="languages" aria-label="Languages"><span>Language / 语言</span>' + "".join(links) + "</nav>"


def panel(title, paragraphs):
    return '<section class="panel"><h2>' + escape(title) + '</h2>' + "".join('<p>' + escape(text) + '</p>' for text in paragraphs) + '</section>'


def shell(section, locale, body):
    item = CONTENT[locale]
    title = escape(item["nav"][section])
    nav_links = "".join(
        f'<a href="{page_url(name, locale)}"' + (' aria-current="page"' if name == section else "") + f'>{escape(item["nav"][name])}</a>'
        for name in SECTIONS
    )
    return f'''<!doctype html>
<html lang="{escape(item['lang'])}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><title>{title} | UnicLife Key Cabinet</title><meta name="description" content="{escape(item['intros'][section])}"><link rel="icon" href="../../favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../../assets/site.css"><link rel="stylesheet" href="../../assets/locales.css"></head><body>
<header class="top"><div class="wrap"><a class="brand" href="../../">UnicLife Key Cabinet</a><nav class="nav" aria-label="Main navigation">{nav_links}</nav></div></header>
<main class="wrap"><div class="hero"><span class="eyebrow">UnicLife</span><h1>{title}</h1><p class="lede">{escape(item['intros'][section])}</p><p class="meta">{escape(item['updated'])}</p></div>{language_nav(section, locale)}<div class="stack">{body}</div></main>
<footer class="footer"><div class="wrap"><span>© 2026 UnicLife Key Cabinet</span><nav aria-label="Footer navigation"><a href="../../">Home</a>{nav_links}</nav></div></footer></body></html>
'''


def render_privacy(locale):
    return "".join(panel(title, paragraphs) for title, paragraphs in CONTENT[locale]["privacy"])


def render_choices(locale):
    item = CONTENT[locale]["choices"]
    link = f'<p><a class="button" href="mailto:{EMAIL}?subject=UnicLife%20privacy%20request">{escape(item["button"])}</a></p>'
    return panel(item["request_title"], item["request"]) + link + panel(item["rights_title"], item["rights"]) + panel(item["ads_title"], item["ads"])


def render_delete(locale):
    item = CONTENT[locale]["delete"]
    link = f'<p><a class="button" href="mailto:{EMAIL}?subject=Delete%20my%20UnicLife%20Key%20Cabinet%20account">{escape(item["button"])}</a></p>'
    return panel(item["request_title"], item["request"]) + link + panel(item["app_title"], item["app"]) + panel(item["data_title"], item["data"])


def render_support(locale):
    item = CONTENT[locale]["support"]
    link = f'<p><a class="button" href="mailto:{EMAIL}?subject=UnicLife%20Key%20Cabinet%20support">{escape(item["button"])}</a></p>'
    return panel(item["contact_title"], item["contact"]) + link + panel(item["privacy_title"], item["privacy"])


def main():
    renderers = {"privacy": render_privacy, "privacy-choices": render_choices, "delete-account": render_delete, "support": render_support}
    for locale in LOCALE_ORDER[1:]:
        for section in SECTIONS:
            destination = ROOT / section / locale / "index.html"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(shell(section, locale, renderers[section](locale)), encoding="utf-8")
    for section in SECTIONS:
        destination = ROOT / section / "index.html"
        source = destination.read_text(encoding="utf-8")
        if "assets/locales.css" not in source:
            source = source.replace('href="../assets/site.css">', 'href="../assets/site.css"><link rel="stylesheet" href="../assets/locales.css">', 1)
        if 'class="languages"' not in source:
            links = [f'<a href="./" aria-current="page">{LOCALE_NAMES["en-us"]}</a>']
            links += [f'<a href="./{locale}/" lang="{CONTENT[locale]["lang"]}">{escape(LOCALE_NAMES[locale])}</a>' for locale in LOCALE_ORDER[1:]]
            nav = '<nav class="languages" aria-label="Languages"><span>Language / 语言</span>' + "".join(links) + '</nav>'
            source, count = re.subn(r'(<main class="wrap"><div class="hero">.*?</div>)', lambda match: match.group(1) + nav, source, count=1, flags=re.DOTALL)
            if count != 1:
                raise ValueError(f"Could not insert language navigation into {destination}")
        destination.write_text(source, encoding="utf-8")
    print(f"Generated {(len(LOCALE_ORDER) - 1) * len(SECTIONS)} localized pages")


if __name__ == "__main__":
    main()
