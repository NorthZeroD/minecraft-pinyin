import os
from pypinyin import lazy_pinyin, load_phrases_dict, Style
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict


def dict_generate(
    minecraft_version: str, lang_json: dict, output_dir: str = "output"
) -> None:
    print("[词典] 开始生成Rime词典...")

    cc_cedict.load()
    load_phrases_dict(phrases_dict)
    result_dict = {}

    for k, v in lang_json.items():
        if (
            not k.startswith("item.minecraft.")
            and not k.startswith("block.minecraft.")
            and not k.startswith("effect.minecraft.")
            and not k.startswith("enchantment.minecraft.")
            and not k.startswith("entity.minecraft.")
        ):
            continue
        try:
            pinyin_list = lazy_pinyin(v, style=Style.TONE, errors="exception")
            pinyin_str = " ".join(pinyin_list)
            result_dict.update({v: pinyin_str})
        except Exception as e:
            pass

    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/minecraft.dict.yaml", "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write('name: "Minecraft Dictionary"\n')
        f.write(f'version: "{minecraft_version}"\n')
        f.write("sort: by_weight\n")
        f.write("...\n")
        for k, v in result_dict.items():
            f.write(f"{k}\t{v}\n")

    print(f"[词典] 已生成词典并保存到 {output_dir}/minecraft.dict.yaml")
