import download
from Formatter import Formatter
from lang_generate import lang_generate
from pack_generate import pack_generate
from dict_generate import dict_generate
from minecraft_versions import (
    get_minecraft_versions,
    get_release_versions,
    get_snapshot_versions,
)
from batch import batch
from batch_all import batch_all

question = """
你想做什么?
1. 生成资源包和Rime词库 (默认)
2. 生成资源包
3. 生成Rime词库
4. 批量生成(单版本)
5. 批量生成(全版本，慎选)

* 直接回车以选择默认项"""

choices = ["", "1", "2", "3", "4", "5"]


def main() -> None:
    print(
        "欢迎使用 Minecraft Pinyin 生成器！\nhttps://github.com/NorthZeroD/minecraft-pinyin"
    )

    print(question)
    a = input("[用户输入] 你的选择: ")
    while True:
        if a in choices:
            break
        a = input("[用户输入] 无此选项。请重新输入: ")

    if a == "4":
        batch()
        return

    if a == "5":
        batch_all()
        return

    if a == "3":
        version_manifest_json = download.get_version_manifest_json()
        minecraft_versions = get_minecraft_versions(version_manifest_json)
        latest_minecraft_version = minecraft_versions[0]
        latest_zhcn_lang_json = download.get_zhcn_lang_json(
            latest_minecraft_version, f"download/{latest_minecraft_version}"
        )
        dict_generate(latest_minecraft_version, latest_zhcn_lang_json)
        print("[结束] 任务已完成。请检查 'output' 文件夹。")
        return

    version_manifest_json = download.get_version_manifest_json()
    minecraft_versions = get_minecraft_versions(version_manifest_json)
    latest_minecraft_version = minecraft_versions[0]
    release_versions = get_release_versions(minecraft_versions)
    snapshot_versions = get_snapshot_versions(minecraft_versions)
    for i in range(5):
        print(f"{release_versions[i]}\t\t{snapshot_versions[i]}")
    mcv = input(f"[用户输入] 输入一个MC版本号 ({latest_minecraft_version}): ")
    if mcv == "":
        mcv = version_manifest_json["latest"]["snapshot"]
    zhcn_lang_json = download.get_zhcn_lang_json(mcv, f"download/{mcv}")
    formatter = Formatter()
    formatter.run()
    lang_generate(zhcn_lang_json, mcv, formatter)
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
    if a == "2":
        print("[结束] 任务已完成。请检查 'output' 文件夹。")
        return

    latest_zhcn_lang_json = download.get_zhcn_lang_json(
        latest_minecraft_version, f"download/{latest_minecraft_version}"
    )
    dict_generate(latest_minecraft_version, latest_zhcn_lang_json)
    print("[结束] 任务已完成。请检查 'output' 文件夹。")


if __name__ == "__main__":
    main()
