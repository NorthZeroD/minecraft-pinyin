import download
from Formatter import Formatter, format_codes, format_converters
from lang_generate import lang_generate
from pack_generate import pack_generate
from dict_generate import dict_generate
from minecraft_versions import get_minecraft_versions
from copy import deepcopy


def batch() -> None:
    version_manifest_json = download.get_version_manifest_json()
    minecraft_versions = get_minecraft_versions(version_manifest_json)
    latest_minecraft_version = minecraft_versions[0]
    dict_generate(latest_minecraft_version)
    zhcn_lang_json = download.get_zhcn_lang_json(latest_minecraft_version)

    formatter = Formatter()
    formatter.left_format_code = "src"
    formatter.left_converter = format_converters["src"]

    for fc in format_codes:
        formatter.right_format_code = fc
        formatter.right_converter = format_converters[fc]
        lang_generate(deepcopy(zhcn_lang_json), latest_minecraft_version, formatter)
        lfc = formatter.left_format_code
        rfc = formatter.right_format_code
        base_resourcepack_name = (
            f"Pinyin_Resource_Pack_{latest_minecraft_version}_{lfc}_{rfc}"
        )
        base_zhcn_lang_json_name = f"zh_cn_{latest_minecraft_version}_{lfc}_{rfc}"
        pack_generate(
            latest_minecraft_version,
            base_resourcepack_name,
            base_zhcn_lang_json_name,
            "zh_cn",
            formatter,
            minecraft_versions,
        )

    print("[结束] 任务已完成。请检查 'output' 文件夹。")


if __name__ == "__main__":
    batch()
