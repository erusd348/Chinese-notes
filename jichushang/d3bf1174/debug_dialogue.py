import re
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Find all play() calls with 李钟文
target = '李钟文'
for m in re.finditer(r"play\('([^']*" + target + r"[^']*)'\)", html):
    s = m.group(1)
    if '糖醋里脊' in s:
        print('=== Found dialogue line ===')
        idx = m.start()
        ctx = html[max(0,idx-10):idx+len(s)+30]
        print(f'HTML context: {repr(ctx)}')
        print()
        print(f'Play param: {repr(s)}')
        print()
        # Check for problematic characters
        for i, ch in enumerate(s):
            if ord(ch) in (0x22, 0x27, 0x201c, 0x201d, 0x2018, 0x2019):
                print(f'  Quote at pos {i}: U+{ord(ch):04X} = {repr(ch)}')
    else:
        print(f'Other 李钟文 line: {s[:40]}...')
