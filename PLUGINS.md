# Plugins

This repo offers the [Taste Skill](https://github.com/Leonxlnx/taste-skill)
plugin (MIT, by leonxlnx): art direction for websites, product pages, dashboards
and app screens, with a real-browser inspector. It fits the landing page in
`index.html`.

## Codex

[`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json) lists
`taste-skill` as available to install from `Leonxlnx/taste-skill@main`. Open the
repo in Codex and install **Taste Skill** from the plugin list (category: Design).

## Claude Code

Inside Claude Code:

```sh
/plugin marketplace add Leonxlnx/taste-skill
/plugin install taste-skill@taste-skill
```

To have Claude Code offer it automatically to anyone who opens this repo, add
this to `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "taste-skill": {
      "source": { "source": "github", "repo": "Leonxlnx/taste-skill" }
    }
  },
  "enabledPlugins": {
    "taste-skill@taste-skill": true
  }
}
```

Then ask for design work, e.g. *"Redesign index.html so it doesn't look
AI-made."* The skill (`design-taste-frontend`) loads automatically.

## Versioning

The marketplace entry tracks upstream `main`, so updates land without a change
here. Set `ref` to a tag to pin a fixed version.
