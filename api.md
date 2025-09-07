**Overview**
- Discord bot with prefix and slash commands, multi-language (i18n), Terms gate, and a persistent Giveaway system with admin tools and a time worker.

**Requirements**
- Node.js 18+
- MariaDB or MySQL
- Discord Bot Token

**Install**
- Create `.env` with:
  - `TOKEN=your_discord_bot_token`
  - `DB_HOST=127.0.0.1`
  - `DB_USER=root`
  - `DB_PASS=...`
  - `DB_NAME=whitecatdata`
  - Optional: `DB_CLIENT=mariadb|mysql2`, `DEFAULT_LANG=en-US`, `PREFIX=!`
- Install deps: `npm i discord.js mariadb mysql2 yaml dotenv`

**Configure**
- `src/config.json`
  - `app.prefix`: default prefix for prefix commands
  - `app.defaultLanguage`: default i18n (e.g. `en-US`)
  - `app.ownerIds`: array of owner user IDs
  - `database.client`: `mariadb` or `mysql2`, `poolMax`: pool size

**Run**
- `node src/bot.js` (or `bash run.sh`)
- Startup does:
  - DB connectivity check and table ensure
  - Seed current guilds into `guilds`
  - Start time jobs, prefix system, slash system, and event handlers

**Slash Commands**
- `avatar`: Show user/server avatar with toggle buttons
- `banner`: Show user/server banner with toggle buttons
- `cgiveway`: Create a giveaway via modal
  - Modal (uses user language): Duration (`10m`, `2h`, `1d2h`), Winners (default 1), Prize, Description
  - Posts embed (uses guild language): Ends, Hosted by, Entries, Winners, created timestamp
  - Buttons: `Join`, `⚙️` Settings (admin-only panel, ephemeral)

**Prefix Commands**
- `!avatar` (alias `!av`)
- `!banner` (alias `!baner`)
- `!sync` / `!sync guild` (owner-only): register slash globally or for current guild

**Giveaway Flow**
- Create: `/cgiveway` -> modal -> embed with `Join` + `⚙️`
- Join: users click `Join`, Entries increases live
- Settings (admin-only, ephemeral):
  - `End` now
  - `Edit Time` (+/- like `+10m`, `-5m`)
  - `Delete` giveaway (marks cancelled and removes message when possible)
- Auto end: time worker runs every 30s to end expired giveaways
- On end:
  - Original embed keeps content, all buttons are removed
  - A new Winners embed is posted with timestamp, first-winner avatar, and two reroll buttons:
    - `🔁 reroll`: reroll excluding currently selected winners (shrinks pool)
    - `👑 keep`: reroll keeping previous winners in pool

**Data Model (Core)**
- `guilds(guild_id PK UNIQUE, prefix, language)`
- `users(user_id UNIQUE, term TINYINT(1), join_at TIMESTAMP)`
- `giveaways(id, guild_id, channel_id, message_id, winners_message_id, creator_id, prize, description, winners_count, allow_multi_win, start_time, end_time, status, winner_ids JSON)`
- `giveaway_entries(id, giveaway_id, user_id, joined_at)` (unique (giveaway_id, user_id))
- `giveaway_excluded(giveaway_id, user_id)` (accumulated excluded winners for reroll-exclude)

**i18n & Terms**
- Language files: `src/language/en-US.yml`, `src/language/vi.yml`
- Default language: `config.app.defaultLanguage` or `DEFAULT_LANG` (fallback `en-US`)
- Slash UI (modals/ephemeral): uses user’s Discord locale (`interaction.locale`)
- Public guild content (embeds): uses guild language from DB or guild locale
- Terms gate:
  - Prefix: uses guild language
  - Slash: uses user language
  - Terms image picker supports `en-US.png`, `en-us.png`, `en.png` with sensible fallbacks

**Folder Structure**
- `src/command/prefix/*`: prefix commands
- `src/command/slash/*`: slash commands
- `src/function/*`: core systems (prefix, slash, event, time, language, wallet, ...)
- `src/module/event/*`: interaction handlers (toggles, giveaway admin, terms, ...)
- `src/module/time/*`: scheduled jobs (giveaway worker)
- `src/language/*`: i18n (YAML)
- `src/image/terms/*`: Terms images

**Common Tasks**
- Sync slash: `!sync` (global) or `!sync guild` (current guild)
- Change per-guild prefix: use prefix ctx helper `setGuildPrefix`
- Set per-guild language: use prefix ctx helper `setGuildLanguage`

**Troubleshooting**
- FK error on giveaways: ensure guild seeding ran (startup) or the bot joined event fired
- Terms image missing: ensure `src/image/terms/en-US.png` exists (fallbacks apply)
- Missing permissions: channel needs `ViewChannel`, `SendMessages`, `SendMessagesInThreads`

**License**
- Internal project; no license header included by default

