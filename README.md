# Bali product demand (Google Ads Keyword Planner, 3 Nov 2026)

Goal: find products with buyer demand in Bali that you can source locally, photograph and sell with Google Search ads. Coffee, and niches where Shopee or Tokopedia win on price, are left out.

## Files

- `bali-bofu-keywords.xlsx`: the main workbook.
  - **Niche summary**: 21 niches ranked by monthly searches, with top bids and a verdict for each.
  - **Keywords (21 niches)**: 270 buyer-intent keywords with language, intent, search range, Google's average, competition and bids.
  - **Codex extra niches** and **Keywords (Codex niches)**: 15 more niches Codex suggested, 180 keywords, same columns.
- `bali-demand-deck.html`: the slide deck, one slide per niche, ordered by monthly searches.
- `raw-keyword-planner/`: the original Keyword Planner exports (historical metrics for Bali, Oct 2025 to Sep 2026; UTF-16, tab-separated).
- `keyword-lists/`: the keywords tested, one niche per line.
- `codex/`: the prompt sent to Codex and its answer.

## How to read the numbers

- **Avg monthly searches** is Google's own average for Bali. This account has no ad spend, so Google rounds each keyword to a range midpoint: 50, 500, 5,000 or 50,000. Treat the figures as order of magnitude.
- **Top-of-page bids** show what advertisers pay for a click at the top of the results. High bids suggest searches that turn into sales.
- **Verdicts** state what the data shows. Anything marked "Suggestion" is a judgement call.
- **Near-me searches 1K+**: flowers, pet food and birthday cake have a "terdekat" (near me) search with 1K or more searches a month. Those searchers are best reached with a Google Business Profile linked to your ads.
- **Exact per-keyword averages** unlock in Keyword Planner once the account has spent on ads. Then re-run "Get search volume and forecasts" with the lists in `keyword-lists/`, location set to Bali.

## Where to start

Most searches: pet food (62,200), birthday cake (56,700), souvenirs (27,150), kebaya (16,750), flowers (13,900), batu paras (12,700), e-bikes (12,650), plants (12,300) and commercial fridges (12,250).

Highest bids, a sign that searches turn into sales: dog food (IDR 78K), genset bali (IDR 50.2K), tangki air (IDR 44.1K), ev charger (IDR 41.8K), hampers (IDR 38.4K), solar and CCTV installation (IDR 32.8K).

Wine can't be advertised on Google in Indonesia: Google's alcohol policy allows 0% alcohol there.
