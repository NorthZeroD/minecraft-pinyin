import os
import json
import shutil
from pathlib import Path
from pack_meta import get_pack_meta
from Formatter import Formatter, format_maps


def pack_generate(
    minecraft_version: str,
    base_resourcepack_name: str,
    base_source_lang_json_name: str,
    base_target_lang_json_name: str,
    formatter: Formatter,
    minecraft_versions: list,
    output_dir_root: str = "output",
) -> None:
    print("[资源包] 开始生成资源包...")

    output_dir_sub = Path(output_dir_root) / minecraft_version
    output_dir_rp = output_dir_sub / base_resourcepack_name
    output_lang_dir = output_dir_rp / "assets/minecraft/lang"

    os.makedirs(output_lang_dir, exist_ok=True)

    l = format_maps[formatter.left_content_code]
    r = format_maps[formatter.right_content_code]
    if formatter.right_content_code == "none":
        desc = f"{l}\nNorthZeroD/minecraft-pinyin"
    else:
        desc = f"{l} | {r}\nNorthZeroD/minecraft-pinyin"
    pack_meta = get_pack_meta(minecraft_version, desc, minecraft_versions)
    with open(output_dir_rp / "pack.mcmeta", "w", encoding="utf-8") as f:
        json.dump(pack_meta, f, ensure_ascii=False, indent=2)

    shutil.copy(
        output_dir_sub / f"{base_source_lang_json_name}.json",
        output_lang_dir / f"{base_target_lang_json_name}.json",
    )
    shutil.copy("icon/pack.png", output_dir_rp)

    shutil.make_archive(str(output_dir_rp), "zip", output_dir_rp)
    shutil.rmtree(output_dir_rp)
    print(f"[资源包] 已生成资源包并保存到 {output_dir_rp}.zip")
