# Deploying

The site is hosted on Vercel in the **crescendo rose** team, project
**crescendorosesite-2**, serving www.crescendorose.com and
www.crescendoroseentertainment.com.

The project is connected to this GitHub repository:

- Pushing to the production branch (`claude/setup-mcp-servers-forsja`, the
  repo's default branch) deploys straight to the live site.
- Pushing to any other branch creates a preview deployment with its own URL.

Site settings live in `vercel.json`. There is no build step: `index.html` and
`images/` are served as static files.

If a push does not show up as a deployment, first check that the Vercel GitHub app
is installed on `crescendoroseentertainment-sudo` with access to this repo, and
that the project's Settings → Git page lists this repository.
