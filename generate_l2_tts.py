"""Generate Edge TTS audio for jichushang L2, then deploy to GitHub."""

import re, os, json, hashlib, asyncio, edge_tts

LESSON_DIR = r"D:\工作空间\2026-06-05-23-40-19\Chinese-notes\jichushang\l2"
HTML_PATH = os.path.join(LESSON_DIR, "index.html")

with open(HTML_PATH, encoding='utf-8') as f:
    html = f.read()

# Extract all play() calls
play_calls = re.findall(r"play\('([^']+)'\)", html)
print(f"Total play() calls: {len(play_calls)}", flush=True)

# Same regex as the play() function
prefix_re = re.compile(r'^[A-Za-z\u4e00-\u9fff]+\s*[\uFF1A:]\s*')

def clean_text(t):
    t = prefix_re.sub('', t)
    t = re.sub(r'\[\d+\]', '', t)
    t = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', t).strip()
    return t

# Deduplicate
clean_map = {}
for call in play_calls:
    ct = clean_text(call)
    if ct:
        clean_map[ct] = call

print(f"Unique texts for TTS: {len(clean_map)}", flush=True)

# Generate audio
AUDIO_DIR = os.path.join(LESSON_DIR, "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

async def gen(text, path):
    c = edge_tts.Communicate(text, "zh-CN-XiaoxiaoNeural")
    await c.save(path)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

new_audiodata = {}
for i, (ct, orig) in enumerate(clean_map.items()):
    ext = hashlib.md5(ct.encode()).hexdigest()[:8]
    fname = f"l2_{i:04d}_{ext}.mp3"
    out_path = os.path.join(AUDIO_DIR, fname)
    
    if not os.path.exists(out_path):
        print(f"  Generating [{i+1}/{len(clean_map)}]: {ct[:40]}...", flush=True)
        try:
            loop.run_until_complete(gen(ct, out_path))
        except Exception as e:
            print(f"  ERROR: {e}", flush=True)
            continue
    else:
        print(f"  Skipping [{i+1}/{len(clean_map)}] (exists): {ct[:40]}...", flush=True)
    
    new_audiodata[ct] = fname

print(f"\nGenerated audio: {len(new_audiodata)} files", flush=True)

# Write audiodata.js (BEFORE verification to ensure it's always saved)
with open(os.path.join(AUDIO_DIR, "audiodata.js"), "w", encoding="utf-8") as f:
    f.write("var AUDIODATA=" + json.dumps(new_audiodata, ensure_ascii=False) + ";")
print("audiodata.js written!", flush=True)

# Verify
all_ok = True
for call in play_calls:
    k = clean_text(call)
    if k not in new_audiodata:
        print(f"  FAIL: {call[:40]} -> {k[:40]} not in audiodata", flush=True)
        all_ok = False

if all_ok:
    print(f"All {len(play_calls)} play() calls have matching audio!", flush=True)
else:
    print("SOME FAILURES ABOVE!", flush=True)
