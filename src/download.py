import requests
import json
import os
from pathlib import Path


def hitcache(filepath: str | Path) -> dict:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.loads(f.read())
    raise Exception(f"缓存未命中: {filepath}")


def get_json_file(
    filename: str,
    url: str,
    download_dir: str = "download",
    download_dir_sub: str = "",
) -> dict:
    download_path = Path(download_dir) / download_dir_sub
    os.makedirs(download_path, exist_ok=True)
    filepath = download_path / filename
    try:
        j = hitcache(filepath)
        print(f"[下载] 命中缓存 {filepath}")
        return j
    except:
        pass
    print(f"[下载] 开始下载文件 {filename}")
    try:
        r = requests.get(url)
        j = json.loads(r.text)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(j, f, ensure_ascii=False, indent=2)
        print(f"[下载] 已保存到 {filepath}")
        return j
    except Exception as e:
        raise Exception(f"[错误] 网络故障: {str(e)}")


def get_version_manifest_json(
    download_dir: str = "download",
    download_dir_sub: str = "",
) -> dict:
    version_manifest_json = get_json_file(
        "version_manifest.json",
        "https://piston-meta.mojang.com/mc/game/version_manifest.json",
        download_dir,
        download_dir_sub,
    )
    return version_manifest_json


def get_version_json(
    minecraft_version: str,
    download_dir: str = "download",
    download_dir_sub: str = "",
) -> dict:
    version_manifest_json = get_version_manifest_json()
    for v in version_manifest_json["versions"]:
        if v["id"] == minecraft_version:
            url = v["url"]
            version_json = get_json_file(
                f"{minecraft_version}.json", url, download_dir, download_dir_sub
            )
            return version_json
    raise Exception(f"[错误] 版本不存在: {minecraft_version}")


def get_asset_index_json(
    minecraft_version: str,
    download_dir: str = "download",
    download_dir_sub: str = "",
) -> dict:
    version_json = get_version_json(minecraft_version, download_dir)
    filename = f'{version_json["assets"]}.json'
    url = version_json["assetIndex"]["url"]
    asset_index_json = get_json_file(filename, url, download_dir, download_dir_sub)
    return asset_index_json


def get_zhcn_lang_json(
    minecraft_version: str,
    download_dir: str = "download",
    download_dir_sub: str = "",
) -> dict[str, str]:
    asset_index_json = get_asset_index_json(
        minecraft_version, download_dir, "assetIndex"
    )
    zhcn_lang_hash = asset_index_json["objects"]["minecraft/lang/zh_cn.json"]["hash"]
    zhcn_lang_json = get_json_file(
        "zh_cn.json",
        f"https://resources.download.minecraft.net/{zhcn_lang_hash[0:2]}/{zhcn_lang_hash}",
        download_dir,
        download_dir_sub,
    )
    return zhcn_lang_json


def get_zhhk_lang_json(
    minecraft_version: str,
    download_dir: str = "download",
    download_dir_sub: str = "",
) -> dict[str, str]:
    asset_index_json = get_asset_index_json(minecraft_version, download_dir)
    zhhk_lang_hash = asset_index_json["objects"]["minecraft/lang/zh_hk.json"]["hash"]
    zhhk_lang_json = get_json_file(
        "zh_hk.json",
        f"https://resources.download.minecraft.net/{zhhk_lang_hash[0:2]}/{zhhk_lang_hash}",
        download_dir,
        download_dir_sub,
    )
    return zhhk_lang_json


if __name__ == "__main__":
    pass
