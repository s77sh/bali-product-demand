# Bali product demand: what people in Bali search to buy (Google Keyword Planner, 3 Nov 2026)

On 3 November 2026 I pulled 450 buyer keywords for Bali from Keyword Planner, with Claude doing the runs. **Pet food and birthday cake came out on top.**

The question behind it: **which products can you source in Bali, photograph and sell with Search ads?** So coffee is out, and so is anything Shopee or Tokopedia sell cheaper.

## Where to start

Here are the niches with the most searches, Google's monthly average for Bali (October 2025 to September 2026):

| Niche | Searches a month |
|---|---|
| Pet food | 62,200 |
| Birthday cake | 56,700 |
| Souvenirs | 27,150 |
| Kebaya | 16,750 |
| Flowers | 13,900 |
| Batu paras (carved stone) | 12,700 |
| E-bikes | 12,650 |
| Plants | 12,300 |
| Commercial fridges | 12,250 |

And the highest top-of-page bids, **what advertisers will pay for one click** at the top of the results:

| Keyword | Top-of-page bid |
|---|---|
| dog food | IDR 78K |
| genset bali | IDR 50.2K |
| tangki air | IDR 44.1K |
| ev charger | IDR 41.8K |
| hampers | IDR 38.4K |
| solar and CCTV installation | IDR 32.8K |

One you can't advertise: wine. Google's alcohol policy only allows 0% alcohol ads in Indonesia.

## How to read the numbers

**Treat every volume as an order of magnitude.** The account has no ad spend, so Google rounds each keyword to a range midpoint: 50, 500, 5,000 or 50,000.

Each verdict in the workbook says what the data shows. Anything marked "Suggestion" is **my own call**.

Flowers, pet food and birthday cake each have a "terdekat" (near me) search above 1K a month. **Those buyers want a shop on the map**, so link a Google Business Profile to your ads.

Exact averages show up **once the account spends on ads**. Then run "Get search volume and forecasts" again with `keyword-lists/`, location Bali.

## Files

| File | What's in it |
|---|---|
| `bali-bofu-keywords.xlsx` | The main workbook. "Niche summary" ranks 21 niches with top bids and a verdict each; "Keywords (21 niches)" has their 270 keywords with language, intent, range, average, competition and bids. Two more sheets hold 15 niches Codex suggested and their 180 keywords |
| `bali-demand-deck.html` | The slide deck, one slide per niche, ordered by searches |
| `raw-keyword-planner/` | The original exports (UTF-16, tab-separated) |
| `keyword-lists/` | The keywords tested, one niche per line |
| `codex/` | The prompt sent to Codex and its answer |

## FAQ

### Which products have the most search demand in Bali?

**Pet food, at about 62,000 searches a month**, then birthday cake at about 57,000. Souvenirs, kebaya and flowers follow.

### Is this a list of business ideas for Bali?

Partly. It shows what people search to buy and what advertisers pay per click, which is the demand half. **Margins, suppliers and competition are still yours to check.**

### How accurate are the numbers?

Rounded. With no ad spend, Google gives each keyword a range midpoint, so **a keyword shown as 5,000 might really get 1,200, or 9,000**.

### Can I run the same research for another city in Indonesia?

Yes. Load `keyword-lists/` into Keyword Planner and **set the location to that city**.

## Related repos

| Repo | What it is |
|---|---|
| [claude-seo-skills-benchmark](https://github.com/s77sh/claude-seo-skills-benchmark) | 5 Claude Code SEO skill packs tested on 20 planted problems |
| [claude-random-numbers](https://github.com/s77sh/claude-random-numbers) | Which number Claude picks when you ask for a random one |
| [interview-prep-pack](https://github.com/s77sh/interview-prep-pack) | A Claude Code skill that builds interview prep from your own resume |
| [viral-reel-playbook](https://github.com/s77sh/viral-reel-playbook) | A Claude Code skill for Reels, TikTok and Shorts scripts |

What each one is for: [saeedseo.com/repos/](https://saeedseo.com/repos/).

## Author

Saeed Shahriar, senior SEO and growth marketer. [saeedseo.com](https://saeedseo.com)
