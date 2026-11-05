# Ham Radio Directory

An open directory of amateur radio clubs, personal radio sites, ham media, manufacturers, and associations, maintained openly so it does not go stale the way earlier lists did.

## Why this directory exists

Two earlier lists on GitHub did this job well, and neither is maintained as a club directory any more: [kyleterry/awesome-radio](https://github.com/kyleterry/awesome-radio) (2014, ham section only national association links) and [mcaserta/awesome-amateur-radio](https://github.com/mcaserta/awesome-amateur-radio) (organisations only, no club-level contacts). This directory carries that job on. The full story is on bg7bag.com: [Carrying On Two Good Lists That Stopped](https://bg7bag.com/carrying-on-two-good-lists/).

The same data is published as a searchable directory on bg7bag.com: https://bg7bag.com/tools/ham-links/

## What is listed

Official homepages only. This directory does **not** publish email addresses.

Each entry has: name, category (club, personal, media, manufacturer, or association), country, official website, language, and the month it was last verified.

## How to add, correct, or remove an entry

Email is the fastest way, and no GitHub account is needed. Just send the club or site name and its official website to contact@bg7bag.com, and we will do the rest: check that the site is live and that it is the club or site's own official website, then add it.

You can also open an issue or a pull request on GitHub with the same information.

Any club, site, or outlet can ask to be corrected or removed at any time, by email or on GitHub, and we will do so promptly.

## Rules

- Official websites only. No email addresses, no personal contact details.
- Every entry is added only with the club or site's permission, and only after we have checked it by hand. We do not copy entries from other lists, and we do not add entries by scraping.
- Permission usually comes as a reply to our email, but email is not the only way: it can also come through a submission, the site's own contact form, or a GitHub issue or pull request. In every case, no permission means no listing.
- Every entry is verified before it is listed, and the verified month is shown. A site that does not reply to a verification request is not listed.
- This directory is a listing, not an endorsement.

## Where this directory is going

This directory is still being collected and organised, and the number of entries is still growing. That is why it lives on bg7bag.com for now, and why an independent domain for it has not been decided yet.

The plan is that, when the directory is large enough, it will move out of bg7bag.com to its own dedicated domain for this ham radio directory. If you have a suggestion for a good domain name for this directory, we would welcome it — please email contact@bg7bag.com or open an issue on GitHub. When the move happens, the current address will redirect, so links to this directory will not break.

## Data

- `clubs.json` — the directory data, one object per entry.
- Fields: `name`, `category`, `country`, `region`, `website`, `contact_page`, `language`, `verified` (YYYY-MM).

## License

MIT. See LICENSE.
