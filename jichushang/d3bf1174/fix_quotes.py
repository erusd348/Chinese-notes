"""Fix ASCII double quotes in dialogue text that break onclick attributes."""

import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Replace ASCII " inside play('...') with Chinese full-width quotes
# The issue: onclick="play('... " ... ')" — the " closes the attribute
# Fix: replace " with Chinese left/right quotes "" (U+201C, U+201D)
# Simple approach: replace all ASCII " inside play() params with full-width quotes

# Find all play('...') calls and fix internal double quotes
def fix_play_matches(m):
    """Replace " inside play('...') with Chinese quotes."""
    inner = m.group(1)
    inner = inner.replace('"', '\u201c')  # Left double quote
    # Actually let's just use \u300c and \u300d (corner brackets)
    # Or simpler: replace inner " with &#34; (HTML entity for ")
    # Or even simpler: replace " with full-width quotes
    # Let me try: replace " with Chinese left/right quotes alternating
    # But that's complex. Let's just use \uff02 (full-width quotation mark)
    inner = inner.replace('"', '\uff02')  # Full-width quotation mark ＂
    return f"play('{inner}')"

# Apply to all play('...') calls
count_before = html.count("play('")
html = re.sub(r"play\('([^']*)'\)", fix_play_matches, html)
count_after = html.count("play('")

print(f"Fixed play() calls: {count_before} -> {count_after}")

# Also fix the same issue in vocab play() calls (糖醋里脊 as a vocab word)
# Check for remaining issues
problematic = 0
for m in re.finditer(r"play\('([^']*)'\)", html):
    inner = m.group(1)
    if '"' in inner:
        problematic += 1
        print(f"  STILL PROBLEMATIC: {inner[:40]}...")

if problematic == 0:
    print("All play() calls are clean!")
else:
    print(f"WARNING: {problematic} play() calls still have double quotes")

# Also check onclick attributes
onclick_issues = html.count('onclick="play(')
if onclick_issues > 0:
    print(f"WARNING: {onclick_issues} onclick=\"play(\" patterns found (potential breakage)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
