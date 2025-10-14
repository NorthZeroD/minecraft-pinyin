import json
import os
from pypinyin import pinyin, lazy_pinyin, Style
from ojson import Json
from pypinyin_dict.phrase_pinyin_data import cc_cedict

def main() -> None:
    cc_cedict.load()

    with open('download/zh_cn.json', 'r', encoding='utf-8') as f:
        lang_json = json.load(f)

    ignore_keys = Json.load_file('ignore_keys.json')

    for k, v in lang_json.items():
        if not k.startswith('item.minecraft.') and not k.startswith('block.minecraft.'):
            continue
        if k in ignore_keys.data()['ignore_keys']:
            continue
        try:
            pinyin_list = lazy_pinyin(v, style=Style.TONE3, neutral_tone_with_five=True, errors='exception')
            pinyin_str = ''.join(pinyin_list)
            lang_json[k] = f"{v} | {pinyin_str}"
        except Exception as e:
            ignore_keys._content['ignore_keys'].append(k)
            print(f"Error processing key {k}: {e}")

    ignore_keys.save_formatted('ignore_keys.json')

    os.makedirs('output', exist_ok=True)
    with open('output/zh_py.json', 'w', encoding='utf-8') as f:
        json.dump(lang_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
