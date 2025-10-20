import requests
import json
import os
class Downloader:
    version_manifest_json: dict
    version_json: dict
    asset_index_json: dict
    lang_json: dict
    selected_version: str
    version_json_url: str
    download_dir: str

    def __init__(self, download_dir: str) -> None:
        self.download_dir = download_dir
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def get_json_file(self, file_name: str, url: str) -> dict:
        try:
            response = requests.get(url)
            data = json.loads(response.text)
            with open(f'{self.download_dir}/{file_name}', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f'Downloaded and saved {self.download_dir}/{file_name}')
            return data
        except Exception as e:
            raise e

    def get_version_manifest_json(self) -> dict:
        try:
            self.version_manifest_json = self.get_json_file('version_manifest.json', 'https://piston-meta.mojang.com/mc/game/version_manifest.json')
            return self.version_manifest_json
        except Exception as e:
            raise Exception(f'Failed to get version manifest json: {str(e)}')

    def select_version(self, selected_version) -> None:
        self.selected_version = selected_version
        for v in self.version_manifest_json['versions']:
            if v['id'] == selected_version:
                self.version_json_url = v['url']
                return
        raise Exception('Version not found: ' + selected_version)

    def get_version_json(self) -> dict:
        try:
            self.version_json = self.get_json_file(f'{self.selected_version}.json', self.version_json_url)
            return self.version_json
        except Exception as e:
            raise Exception(f'Failed to get version json: {str(e)}')

    def get_asset_index_json(self) -> dict:
        try:
            self.asset_index_json = self.get_json_file(f'{self.version_json['assetIndex']['id']}.json', self.version_json['assetIndex']['url'])
            return self.asset_index_json
        except Exception as e:
            raise Exception(f'Failed to get asset index json: {str(e)}')

    def get_lang_json(self) -> dict:
        try:
            self.lang_json = self.get_json_file('zh_cn.json', f'https://resources.download.minecraft.net/{self.asset_index_json['objects']['minecraft/lang/zh_cn.json']['hash'][0:2]}/{self.asset_index_json['objects']['minecraft/lang/zh_cn.json']['hash']}')
            return self.lang_json
        except Exception as e:
            raise Exception(f'Failed to get lang json: {str(e)}')
