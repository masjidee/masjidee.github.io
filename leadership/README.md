# Direct-link leadership assets

These are leadership discussion drafts for the proof of concept / pilot. They are public documents intentionally omitted from site navigation, Starlight search and sitemaps. Noindex metadata requests that search engines omit the HTML pages. This is not authentication: people with a URL or repository access can read and share them.

After merge and a successful manual website deployment:

| Asset | Direct page | Download |
| --- | --- | --- |
| Executive whitepaper | https://masjidee.github.io/docs/leadership/executive-whitepaper/ | https://masjidee.github.io/docs/leadership/masjidee-executive-whitepaper.pdf |
| Detailed whitepaper | https://masjidee.github.io/docs/leadership/detailed-whitepaper/ | https://masjidee.github.io/docs/leadership/masjidee-detailed-whitepaper.pdf |
| Presentation | https://masjidee.github.io/docs/leadership/presentation/ | https://masjidee.github.io/docs/leadership/masjidee-leadership-presentation.pptx |

The deck also has a PDF at https://masjidee.github.io/docs/leadership/masjidee-leadership-presentation.pdf. Speaker notes are available in the editable PowerPoint and under each web slide. The web deck supports arrow-key navigation and fullscreen.

## Sources and updates

`src/data/leadership.json` is the shared editorial source for web pages and all downloads. `scripts/build-leadership-assets.py` creates the PDF papers and editable PowerPoint/PDF deck. Free Python libraries are pinned in `leadership/requirements.txt`. Install them into a local virtual environment if not already available:

```sh
python3 -m venv .venv-leadership
.venv-leadership/bin/pip install -r leadership/requirements.txt
.venv-leadership/bin/python scripts/build-leadership-assets.py
npm run build
npm run check:links
npm run check:leadership
```

The script embeds DejaVu fonts from `/usr/share/fonts/truetype/dejavu` by default. On another system, set `MASJIDEE_FONT_DIR` to a directory containing `DejaVuSans.ttf`, `DejaVuSans-Bold.ttf`, and `DejaVuSerif.ttf`. No paid Office license or external generation service is needed. Generated PDFs and PPTX are committed so standard website CI does not need Python or font installation. Regenerate and commit them whenever the editorial source changes. The verification command checks that their provenance digest matches the JSON source.

Content distinguishes implemented learning and delegated oversight from proposed national attendance aggregation. Google/email are the current sign-in methods, not an assertion that Apple is enabled. A calendar match is an attendance signal, not proof of participation or absence. The policy discussion explicitly includes privileged administrator diagnostics and the current limits on typed memberships. These are presentation drafts, not approved Jamaat policies, production-readiness certification or measured outcome claims.

Do not add a leadership entry to the public sidebar or homepage. Verify direct-link access and ordinary documentation search after changes. PDFs and PowerPoint files can still be redistributed or discovered if linked elsewhere; do not put confidential member data in them.
