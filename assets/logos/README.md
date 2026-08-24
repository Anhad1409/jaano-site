# Brand logos — drop-in slot

Name the file after the brand, lowercase, alphanumerics only:

    zerodha.svg   mobikwik.svg   indusindbank.svg
    adityabirlacapital.svg        bajajfinance.svg

Accepted: `.svg` (preferred), `.png`, `.webp`. Must exceed 2 KB — smaller
files are treated as favicons and ignored.

Rebuild (`cd build && python3 build.py`) and that brand renders as a real
logo in the marquee. Brands without a file render as a typographic chip, so
the row is never broken and never shows a missing image.

**Do not use scraped favicons.** They are 16–48px, often cropped variants of
the real mark, and on a bank-facing page they raise a trademark question.
Use the logo pack from each partnership or marketing agreement.
