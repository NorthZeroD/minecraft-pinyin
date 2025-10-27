import os
from copy import deepcopy
import download
from Formatter import Formatter, format_codes, format_converters
from lang_generate import lang_generate
from pack_generate import pack_generate
from dict_generate import dict_generate
from minecraft_versions import get_minecraft_versions, get_release_versions


def batch_all() -> None:
    version_manifest_json = download.get_version_manifest_json()
    minecraft_versions = get_minecraft_versions(version_manifest_json)
    release_versions = get_release_versions(minecraft_versions)
    latest_minecraft_version = minecraft_versions[0]

    latest_zhcn_lang_json = download.get_zhcn_lang_json(
        latest_minecraft_version, f"download/{latest_minecraft_version}"
    )
    dict_generate(latest_minecraft_version, latest_zhcn_lang_json)

    for mcv in release_versions:
        if os.path.exists(f"output/{mcv}"):
            continue
        zhcn_lang_json = download.get_zhcn_lang_json(mcv, f"download/{mcv}")
        formatter = Formatter()
        formatter.left_content_code = "src"
        formatter.left_converter = format_converters["src"]
        for fc in format_codes:
            if fc == "src" or fc == "none":
                continue
            formatter.right_content_code = fc
            formatter.right_converter = format_converters[fc]
            lang_generate(deepcopy(zhcn_lang_json), mcv, formatter)
            lcc = formatter.left_content_code
            rcc = formatter.right_content_code
            base_resourcepack_name = f"Pinyin_Resource_Pack_{mcv}_{lcc}_{rcc}"
            base_zhcn_lang_json_name = f"zh_cn_{mcv}_{lcc}_{rcc}"
            pack_generate(
                mcv,
                base_resourcepack_name,
                base_zhcn_lang_json_name,
                "zh_cn",
                formatter,
                minecraft_versions,
            )
        if mcv == "1.13":
            break
    print("[结束] 任务已完成。请检查 'output' 文件夹。")


if __name__ == "__main__":
    batch_all()
