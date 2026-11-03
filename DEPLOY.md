# Deploying

The site is hosted on Vercel in the **crescendo rose** team, project
**crescendorosesite-2**, serving www.crescendorose.com and
www.crescendoroseentertainment.com.

Deploys run from the GitHub Action in `.github/workflows/deploy.yml`, which
uses the `VERCEL_TOKEN` repository secret (a Vercel token scoped to the
crescendo rose team):

- Pushing to the production branch (`claude/setup-mcp-servers-forsja`, the
  repo's default branch) deploys straight to the live site.
- Pushing to any other branch creates a preview deployment with its own URL
  (protected by Vercel login; custom domains stay public).

Site settings live in `vercel.json`. There is no build step: `index.html` and
`images/` are served as static files.

If a push does not show up as a deployment, open the repo's **Actions** tab on
GitHub and check the "Deploy to Vercel" run. A failed "Pull project settings"
step usually means `VERCEL_TOKEN` is missing, expired, or not scoped to the
crescendo rose team.
