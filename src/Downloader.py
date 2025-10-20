import requests
import json
import os


class Downloader:
    download_dir: str
    version_manifest_json: dict
    version_json: dict
    asset_index_json: dict
    lang_jsons: dict

    def __init__(self, download_dir: str) -> None:
        self.download_dir = download_dir

    def hitcache(self, filepath: str) -> dict:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return json.loads(f.read())
        raise Exception(f"缓存未命中: {filepath}")

    def get_json_file(self, filename: str, url: str) -> dict:
        filepath = f"{self.download_dir}/{filename}"
        try:
            j = self.hitcache(filepath)
            print(f"命中缓存: {filepath}")
            return j
        except:
            pass
        try:
            r = requests.get(url)
            j = json.loads(r.text)
            with open(
                filepath,
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    j,
                    f,
                    ensure_ascii=False,
                    indent=2,
                )
            print(f"已下载并保存 {filepath}")
            return j
        except Exception as e:
            raise Exception(f"Downloader.get_json_file({filename}, {url}): {str(e)}")

    def get_version_manifest_json(self) -> dict:
        version_manifest_json = self.get_json_file(
            "version_manifest.json",
            "https://piston-meta.mojang.com/mc/game/version_manifest.json",
        )
        return version_manifest_json

    def get_version_json(
        self, minecraft_version: str, version_manifest_json: dict
    ) -> dict:
        for v in version_manifest_json["versions"]:
            if v["id"] == minecraft_version:
                url = v["url"]
                version_json = self.get_json_file(f"{minecraft_version}.json", url)
                return version_json
        raise Exception(f"不存在的版本: {minecraft_version}")

    def get_asset_index_json(self, version_json: dict) -> dict:
        filename = f'{version_json["assets"]}.json'
        url = version_json["assetIndex"]["url"]
        asset_index_json = self.get_json_file(filename, url)
        return asset_index_json

    def get_lang_jsons(self, asset_index_json: dict) -> dict:
        zhcn_hash = asset_index_json["objects"]["minecraft/lang/zh_cn.json"]["hash"]
        zhcn_lang = self.get_json_file(
            "zh_cn.json",
            f"https://resources.download.minecraft.net/{zhcn_hash[0:2]}/{zhcn_hash}",
        )
        zhhk_hash = asset_index_json["objects"]["minecraft/lang/zh_hk.json"]["hash"]
        zhhk_lang = self.get_json_file(
            "zh_hk.json",
            f"https://resources.download.minecraft.net/{zhhk_hash[0:2]}/{zhhk_hash}",
        )
        lang_jsons = {"zh_cn": zhcn_lang, "zh_hk": zhhk_lang}
        return lang_jsons

    def run(self) -> None:
        os.makedirs(self.download_dir, exist_ok=True)
        self.version_manifest_json = self.get_version_manifest_json()
        print(self.version_manifest_json["latest"])
        minecraft_version = input("输入一个MC版本号: ")
        self.download_dir += f"/{minecraft_version}"
        os.makedirs(self.download_dir, exist_ok=True)
        self.version_json = self.get_version_json(
            minecraft_version, self.version_manifest_json
        )
        self.asset_index_json = self.get_asset_index_json(self.version_json)
        self.lang_jsons = self.get_lang_jsons(self.asset_index_json)


if __name__ == "__main__":
    downloader = Downloader("download")
    downloader.run()
