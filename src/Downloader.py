import requests
import json
import os
class Downloader:
    _version_manifest_json: dict = {}
    _version_json: dict = {}
    _asset_index_json: dict = {}
    _lang_json: dict = {}
    _selected_version: str = ''
    _version_json_url: str = ''
    _download_dir: str = 'download'

    def __init__(self, download_dir: str = 'download') -> None:
        self._download_dir = download_dir
        if not os.path.exists(self._download_dir):
            os.makedirs(self._download_dir)

    def _get_json_file(self, file_name: str, url: str) -> dict:
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            with open(f'{self._download_dir}/{file_name}', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Downloaded and saved {self._download_dir}/{file_name}")
            return data
        raise Exception(f"Failed to download {file_name}, status code: {response.status_code}")

    def get_version_manifest_json(self) -> None:
        try:
            self._version_manifest_json = self._get_json_file('version_manifest.json', 'https://piston-meta.mojang.com/mc/game/version_manifest.json')
        except Exception as e:
            raise e

    def select_version(self, selected_version) -> None:
        self._selected_version = selected_version
        for v in self._version_manifest_json['versions']:
            if v['id'] == selected_version:
                self._version_json_url = v['url']
                return
        raise Exception("Version not found: " + selected_version)

    def get_version_json(self) -> None:
        try:
            self._version_json = self._get_json_file(f'{self._selected_version}.json', self._version_json_url)
        except Exception as e:
            raise e

    def get_asset_index_json(self) -> None:
        try:
            self._asset_index_json = self._get_json_file(f'{self._version_json['assetIndex']['id']}.json', self._version_json['assetIndex']['url'])
        except Exception as e:
            raise e

    def get_lang_json(self) -> None:
        try:
            self._lang_json = self._get_json_file('zh_cn.json', f'https://resources.download.minecraft.net/{self._asset_index_json['objects']['minecraft/lang/zh_cn.json']['hash'][0:2]}/{self._asset_index_json['objects']['minecraft/lang/zh_cn.json']['hash']}')
        except Exception as e:
            raise e
