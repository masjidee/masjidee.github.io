# Masjidee website and user guides

Repository: `masjidee/masjidee.github.io`. Public address: **https://masjidee.github.io/**.

Public website and documentation for the Masjidee Android pilot. The application and shared backend remain in a separate private repository. No application credentials, user records or private source belong here.

## What is included

- `/` — Masjidee introduction and feature overview.
- `/get-app/` — invitation-only Android pilot information; no public APK or iOS download.
- `/docs/` — searchable user guides and administrator guides.
- `/support/` — troubleshooting and safe feedback guidance.

The website uses Astro, Starlight and Pagefind. All output is static. No paid search, analytics, server, database or custom domain is needed.

## Develop

Use Node.js 24 or later.

```sh
npm ci
npm run dev
```

The development site uses port 4321 and project base `/`. In the shared environment, the application checkout is `/workspace/SmartLearningBuddy`; this site is `/workspace/masjidee-site`. Run commands in the intended repository.

```sh
npm run build
npm run check:links
npm run preview
```

`check:links` checks generated same-origin links and assets, including the GitHub Pages project base path. It does not make network requests to external websites. In restricted cloud shells, use `npm --cache /workspace/.npm ...` and set `ASTRO_TELEMETRY_DISABLED=1` if the shell cannot write user configuration. Neither setting is required by the hosted site.

## Edit documentation

Guides are Markdown files in `src/content/docs/docs/`. Use `title` and `description` frontmatter. Sidebar entries live in `astro.config.mjs`; landing/support/pilot pages are in `src/pages/`. Site and guide styles are in `src/styles/`.

Check implemented application behavior before updating a guide. Label planned features clearly, particularly iOS, Bluetooth scanning and traffic-aware reminders. Do not publish identifiable location or attendance examples. The phone mockup on the landing page is labelled illustrative, not a live schedule. Maintain factual privacy disclosures when app behavior changes; a pilot feature guide does not establish legal or app-store policy compliance.

## Publish on free GitHub Pages

Publication is deliberately manual for this first review.

1. Merge the reviewed website pull request into `main`.
2. In this repository, open **Settings → Pages → Build and deployment → Source → GitHub Actions**.
3. Open **Actions → Publish website → Run workflow**, selecting `main`.
4. Wait for the build and deployment jobs to succeed. Approve the `github-pages` deployment if GitHub requests it.
5. Open `https://masjidee.github.io/`. Guides are under `/docs/`.

The separate **Website checks** workflow builds and checks links on pull requests and main pushes; it does not publish. Do not run the deployment workflow from an unreviewed branch. No personal access token, hosting secret or domain purchase is needed for GitHub Pages. GitHub service limits and terms still apply.

For later updates, use a branch and PR, check the build, merge, then run the publish workflow again. A future custom domain can be configured in Astro and GitHub Pages without rewriting the guides. Recheck base paths, canonical URLs and the link checker when changing the domain or project path.

## Feedback

Public issues are for website/documentation feedback. Account help and private attendance issues should go to the pilot organizer through the existing private contact channel. Do not post personal information in GitHub issues.
