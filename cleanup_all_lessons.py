#!/usr/bin/env python3
"""
Comprehensive lesson HTML cleaner.
Fixes known data issues and prevents them from recurring.

Issues fixed:
1. Stray [ ] brackets at end of dialogue / narrative text
2. Bare note reference numbers after 。！？ (e.g., ".7", "。8")
3. Superscript note markers in text (¹²³)
4. Stray textbook header text parsed as dialogue
5. Entire .row divs containing textbook headers (e.g., "HORTTERM SPOKEN CHINESE·ELEMENTRY 汉语口语速成 · 基础篇")
"""

import re, json, hashlib, os, asyncio, glob, time

BASE = os.path.dirname(os.path.abspath(__file__))
FIX_LOG = []

def esc_play(s):
    """Escape special chars for JS play() param (single-quoted)."""
    return s.replace("\\", "\\\\").replace("'", "\\'") \
            .replace('"', '\u201c')  # ASCII double quote -> left curly quote

def log(msg):
    print(msg, flush=True)
    FIX_LOG.append(msg)

def clean_play_param(text):
    """Clean a dialogue/narrative text for use in play('...')."""
    original = text
    # 1. Remove stray [ ] at END of text
    text = re.sub(r'[\[\]]+$', '', text)
    # 2. Remove superscript note numbers ¹²³⁴⁵⁶⁷⁸⁹⁰
    text = re.sub(r'[\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u2070]', '', text)
    # 3. Remove bare note reference numbers after 。！？
    text = re.sub(r'(?<=[。！？])\d+(?=[。！？\s\u3000]|$)', '', text)
    text = re.sub(r'(?<=[。！？])\d+(?=[\u4e00-\u9fff])', '', text)
    # 4. Remove "汉语口语速成·基础篇" style headers from play() params
    if '汉语' in text and '口语速成' in text:
        return None  # Skip entirely - it's a header, not content
    return text

# Textbook header patterns for row-level removal (entire .row divs)
TEXTBOOK_HEADER_PATTERNS = [
    '汉语口语速成',
    'HORTTERM SPOKEN CHINESE',
    'HORT',
    'ELEMENTRY',
]

def remove_header_rows(html):
    """Remove entire .row divs that contain textbook header text."""
    alt = '|'.join(re.escape(p) for p in TEXTBOOK_HEADER_PATTERNS)
    pattern = re.compile(
        r'<div class="row[^>]*>(?:(?!</div>).)*?(?:' + alt + r').*?</div>',
        re.DOTALL
    )
    count = 0
    while True:
        m = pattern.search(html)
        if not m:
            break
        html = html[:m.start()] + html[m.end():]
        count += 1
    return html, count

def fix_lesson(num):
    """Fix a single lesson's HTML and audiodata."""
    dir_path = os.path.join(BASE, f'jichushang/l{num}')
    html_path = os.path.join(dir_path, 'index.html')
    ad_path = os.path.join(dir_path, 'audio/audiodata.js')
    
    if not os.path.exists(html_path):
        log(f'L{num}: SKIP (no HTML)')
        return
    
    # Read HTML
    html = open(html_path, encoding='utf-8').read()
    original_html = html
    
    # Read audiodata
    ad = {}
    if os.path.exists(ad_path):
        txt = open(ad_path, encoding='utf-8').read()
        txt = txt.replace('var AUDIODATA=', '', 1).rstrip(';')
        try:
            ad = json.loads(txt)
        except:
            ad = {}
    
    prefix_re = re.compile(r'^[A-Za-z\u4e00-\u9fff]+\s*[\uFF1A:]\s*')
    
    def clean_key(text):
        """Compute the key that play() would use."""
        k = prefix_re.sub('', text)
        k = re.sub(r'\[\d+\]', '', k)
        k = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', k).strip()
        return k
    
    # Find ALL play() calls and fix them
    changes = []
    new_ad_entries = {}
    removed_entries = []
    
    def fix_call(m):
        text = m.group(1)
        fixed = clean_play_param(text)
        
        if fixed is None:
            # This should be skipped entirely
            changes.append(('REMOVE', text[:40]))
            return ''  # Remove the play button entirely
        
        if fixed != text:
            changes.append(('FIX', f'{text[:40]} -> {fixed[:40]}'))
            
            # If the key changed, need to update audiodata
            old_key = clean_key(text)
            new_key = clean_key(fixed)
            if old_key in ad and old_key != new_key:
                new_ad_entries[new_key] = ad[old_key]
                removed_entries.append(old_key)
            
            return f"play('{esc_play(fixed)}')"
        return m.group(0)
    
    html = re.sub(r"play\('([^']+)'\)", fix_call, html)
    
    # Also remove entire .row divs containing textbook headers
    html, removed_rows = remove_header_rows(html)
    if removed_rows:
        changes.append(('ROW_REMOVE', f'{removed_rows} header row(s) removed'))
    
    if not changes:
        log(f'L{num}: no changes needed')
        return
    
    log(f'L{num}: {len(changes)} fix(es)')
    for typ, detail in changes[:5]:
        log(f'  [{typ}] {detail}')
    if len(changes) > 5:
        log(f'  ... and {len(changes)-5} more')
    
    # Update audiodata.js
    if new_ad_entries or removed_entries:
        for k in removed_entries:
            if k in ad:
                del ad[k]
        ad.update(new_ad_entries)
        
        # Also remove any entries whose keys no longer exist (e.g. "汉语口语速成·基础篇")
        html_calls = re.findall(r"play\('([^']+)'\)", html)
        valid_keys = set()
        for c in html_calls:
            k = clean_key(c)
            if k:
                valid_keys.add(k)
        
        removed_from_ad = 0
        for k in list(ad.keys()):
            if k not in valid_keys:
                # Check if there's a close match (same first 10 chars)
                close_match = any(k[:10] == vk[:10] for vk in valid_keys)
                if not close_match:
                    del ad[k]
                    removed_from_ad += 1
        
        if removed_from_ad:
            log(f'  Removed {removed_from_ad} stale audiodata entries')
        
        with open(ad_path, 'w', encoding='utf-8') as f:
            f.write('var AUDIODATA=' + json.dumps(ad, ensure_ascii=False) + ';')
        log(f'  audiodata.js updated ({len(ad)} entries)')
    
    # Write fixed HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    log(f'  HTML written ({len(html)} bytes)')


def regenerate_tts(num):
    """Regenerate TTS for any keys that changed."""
    import ssl
    dir_path = os.path.join(BASE, f'jichushang/l{num}')
    html_path = os.path.join(dir_path, 'index.html')
    ad_path = os.path.join(dir_path, 'audio/audiodata.js')
    
    html = open(html_path, encoding='utf-8').read()
    txt = open(ad_path, encoding='utf-8').read()
    txt = txt.replace('var AUDIODATA=', '', 1).rstrip(';')
    ad = json.loads(txt)
    
    prefix_re = re.compile(r'^[A-Za-z\u4e00-\u9fff]+\s*[\uFF1A:]\s*')
    
    calls = re.findall(r"play\('([^']+)'\)", html)
    ok = 0
    missing = []
    
    for c in calls:
        k = prefix_re.sub('', c)
        k = re.sub(r'\[\d+\]', '', k)
        k = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', k).strip()
        if k in ad:
            fname = ad[k]
            if os.path.exists(os.path.join(dir_path, 'audio', fname)):
                ok += 1
                continue
        missing.append((c, k))
    
    if not missing:
        log(f'L{num}: all {ok}/{ok} keys match')
        return True
    
    log(f'L{num}: {len(missing)} missing TTS entries, generating...')
    
    async def gen(text, path):
        try:
            c = edge_tts.Communicate(text, 'zh-CN-XiaoxiaoNeural')
            await c.save(path)
            return True
        except Exception as e:
            log(f'    ERROR: {e}')
            return False
    
    import edge_tts
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    for orig, k in missing:
        ext = hashlib.md5(k.encode()).hexdigest()[:8]
        existing = [f for f in os.listdir(os.path.join(dir_path, 'audio')) if f.endswith('.mp3')]
        max_idx = 0
        for f in existing:
            try:
                idx = int(f.split('_')[1])
                if idx > max_idx: max_idx = idx
            except: pass
        
        fname = f'l{num}_{max_idx+1:04d}_{ext}.mp3'
        log(f'  Generating: {k[:40]}...', flush=True)
        success = loop.run_until_complete(gen(k, os.path.join(dir_path, 'audio', fname)))
        if success:
            ad[k] = fname
        else:
            log(f'  FAILED: {k[:40]}')
    
    # Write updated audiodata
    with open(ad_path, 'w', encoding='utf-8') as f:
        f.write('var AUDIODATA=' + json.dumps(ad, ensure_ascii=False) + ';')
    
    # Final verify
    ok = 0
    for c in calls:
        k = prefix_re.sub('', c)
        k = re.sub(r'\[\d+\]', '', k)
        k = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', k).strip()
        if k in ad and os.path.exists(os.path.join(dir_path, 'audio', ad[k])):
            ok += 1
    
    log(f'L{num}: final verify {ok}/{len(calls)}')
    return ok == len(calls)


if __name__ == '__main__':
    lessons = list(range(1, 13))
    
    # Phase 1: Fix HTML + audiodata
    log('=== Phase 1: Fix HTML and audiodata ===')
    for num in lessons:
        fix_lesson(num)
    
    # Phase 2: Regenerate TTS for affected lessons
    log('\n=== Phase 2: Regenerate TTS ===')
    for num in lessons:
        regenerate_tts(num)
    
    log('\n=== Summary ===')
    for line in FIX_LOG:
        print(line)
