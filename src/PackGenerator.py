import os
import json
import shutil
from pack_meta import pack_meta


class PackGenerator:
    output_dir: str
    minecraft_version: str
    base_resourcepack_name: str
    base_lang_json_name: str

    def __init__(
        self,
        output_dir,
        minecraft_version: str,
        base_resourcepack_name: str,
        base_lang_json_name: str,
    ) -> None:
        self.output_dir = f"{output_dir}/{minecraft_version}"
        self.minecraft_version = minecraft_version
        self.base_resourcepack_name = base_resourcepack_name
        self.base_lang_json_name = base_lang_json_name

    def run(self) -> None:
        output_rp = f"{self.output_dir}/{self.base_resourcepack_name}"

        os.makedirs(f"{output_rp}/assets/minecraft/lang", exist_ok=True)

        with open(f"{output_rp}/pack.mcmeta", "w", encoding="utf-8") as f:
            json.dump(pack_meta, f, ensure_ascii=False, indent=2)

        shutil.copy(
            f"{self.output_dir}/{self.base_lang_json_name}.json",
            f"{output_rp}/assets/minecraft/lang/zh_cn.json",
        )
        shutil.make_archive(output_rp, "zip", output_rp)
        print(f"已生成并保存 {output_rp}.zip")
