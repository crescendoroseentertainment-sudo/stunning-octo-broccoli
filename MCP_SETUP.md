# MCP server setup

Three MCP servers are configured for this repo in [`.mcp.json`](.mcp.json).
Because that file is project-scoped and committed, anyone who clones the repo
gets the same servers.

| Server | Transport | Auth | Cost |
| --- | --- | --- | --- |
| `playwright` | stdio (`npx @playwright/mcp@latest`) | none | free |
| `composio` | http | OAuth browser sign-in | free tier |
| `firecrawl` | http | `FIRECRAWL_API_KEY` bearer token | free tier |

Perplexity was intentionally left out (paid). See [Adding Perplexity later](#adding-perplexity-later).

## One-time setup

### 1. Firecrawl API key

Get a free key at <https://firecrawl.dev> (Dashboard → API Keys), then export it
so `.mcp.json` can read it. The key is referenced as `${FIRECRAWL_API_KEY}` and
is **never stored in the repo**.

```sh
echo 'export FIRECRAWL_API_KEY="fc-your-key-here"' >> ~/.zshrc   # or ~/.bashrc
source ~/.zshrc
```

Verify it is visible to Claude Code before starting it:

```sh
echo "${FIRECRAWL_API_KEY:?not set}"
```

> Firecrawl's endpoint also works **keyless** at a reduced rate limit, exposing
> only Search, Scrape and Parse. To run without a key, drop the `headers` block
> from the `firecrawl` entry in `.mcp.json`. With a key you get the full tool set.

### 2. Approve the servers

Project-scoped servers require explicit approval the first time, so Claude Code
never runs a server a repo added behind your back. Start Claude Code in this
directory and accept the prompt:

```sh
cd stunning-octo-broccoli
claude
```

Then confirm all three report `✓ Connected`:

```
/mcp
```

### 3. Sign in to Composio

Composio authenticates over OAuth, which needs a browser. Inside Claude Code:

```
/mcp
```

Select **composio** → **Authenticate**. A browser window opens; sign in and
approve. The token is cached locally, so this is a one-time step.

## Test prompts

Run each in Claude Code once the server shows as connected.

**Playwright** — drives a real Chromium browser:

> Use Playwright to open https://example.com, tell me the exact text of the `<h1>`, then take a screenshot and save it as example.png.

**Composio** — check which of your accounts are wired up before doing real work:

> Using Composio, list the toolkits and connected accounts I have available, and tell me which ones are authenticated and ready to use.

**Firecrawl** — scraping and search:

> Use Firecrawl to scrape https://firecrawl.dev and return the page's main content as markdown, then summarize what the product does in three bullets.

## Adding Perplexity later

Perplexity's MCP endpoint needs a paid API key from
<https://perplexity.ai> (Settings → API). Once you have one:

```sh
echo 'export PERPLEXITY_API_KEY="pplx-your-key-here"' >> ~/.zshrc
source ~/.zshrc

claude mcp add -s project -t http perplexity https://api.perplexity.ai/mcp \
  -H 'Authorization: Bearer ${PERPLEXITY_API_KEY}'
```

Quote the header with **single quotes** so the shell leaves `${PERPLEXITY_API_KEY}`
as a literal for Claude Code to expand at runtime — double quotes would bake the
secret into the committed file.

Test prompt:

> Use Perplexity to research what changed in the MCP specification during 2026, with sources.

## Troubleshooting

**`Missing environment variables: FIRECRAWL_API_KEY`** — the variable is not set
in the shell that launched Claude Code. Export it (step 1) and restart Claude Code;
GUI launchers do not always inherit your shell profile.

**`Pending approval`** — expected for project-scoped servers. Run `claude` in this
directory and approve, per step 2.

**Playwright fails to download** — it fetches `@playwright/mcp` from the npm
registry on first run, so it needs npm access. On a machine with a restricted
registry, pre-install it (`npm i -g @playwright/mcp`) and point the config at the
installed binary instead of `npx`.

**Managing servers:**

```sh
claude mcp list              # health check all servers
claude mcp get firecrawl     # inspect one
claude mcp remove firecrawl -s project
```
