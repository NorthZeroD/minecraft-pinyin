import download
from Formatter import Formatter
from lang_generate import lang_generate
from pack_generate import pack_generate
from dict_generate import dict_generate

question = """
你想做什么?
1. 生成资源包和Rime词库 (默认)
2. 生成资源包
3. 生成Rime词库
4. 退出

你的选择: """


def main() -> None:
    a = input(question)
    if a == "4":
        return

    if a == "3":
        version_manifest_json = download.get_version_manifest_json()
        latest_snapshot_version = version_manifest_json["latest"]["snapshot"]
        latest_snapshot_zhcn_lang_json = download.get_zhcn_lang_json(
            latest_snapshot_version, f"download/{latest_snapshot_version}"
        )
        dict_generate(latest_snapshot_version, latest_snapshot_zhcn_lang_json)
        return

    version_manifest_json = download.get_version_manifest_json()
    print(version_manifest_json["latest"])
    mcv = input("输入一个MC版本号: ")
    zhcn_lang_json = download.get_zhcn_lang_json(mcv, f"download/{mcv}")
    formatter = Formatter()
    formatter.run()
    lang_generate(zhcn_lang_json, mcv, formatter)
    lcc = formatter.left_content_code
    rcc = formatter.right_content_code
    base_resourcepack_name = f"Pinyin_Resource_Pack_{mcv}_{lcc}_{rcc}"
    base_zhcn_lang_json_name = f"zh_cn_{mcv}_{lcc}_{rcc}"
    pack_generate(
        mcv, base_resourcepack_name, base_zhcn_lang_json_name, "zh_cn", formatter
    )
    if a == "2":
        return

    latest_snapshot_version = version_manifest_json["latest"]["snapshot"]
    latest_snapshot_zhcn_lang_json = download.get_zhcn_lang_json(
        latest_snapshot_version, f"download/{latest_snapshot_version}"
    )
    dict_generate(latest_snapshot_version, latest_snapshot_zhcn_lang_json)


if __name__ == "__main__":
    main()
