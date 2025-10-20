import os
import json
import shutil
from pack_meta import get_pack_meta


def pack_generate(
    minecraft_version: str,
    base_resourcepack_name: str,
    base_source_lang_json_name: str,
    base_target_lang_json_name: str,
    output_dir_root: str = "output",
) -> None:
    output_dir_sub = f"{output_dir_root}/{minecraft_version}"
    output_dir_rp = f"{output_dir_sub}/{base_resourcepack_name}"

    os.makedirs(f"{output_dir_rp}/assets/minecraft/lang", exist_ok=True)

    pack_meta = get_pack_meta(minecraft_version)
    with open(f"{output_dir_rp}/pack.mcmeta", "w", encoding="utf-8") as f:
        json.dump(pack_meta, f, ensure_ascii=False, indent=2)

    shutil.copy(
        f"{output_dir_sub}/{base_source_lang_json_name}.json",
        f"{output_dir_rp}/assets/minecraft/lang/{base_target_lang_json_name}.json",
    )
    shutil.make_archive(output_dir_rp, "zip", output_dir_rp)
    print(f"已生成并保存 {output_dir_rp}.zip")
