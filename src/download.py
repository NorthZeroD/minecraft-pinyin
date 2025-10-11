from utils import *

def get_version_manifest() -> dict:
    status_code = get_json_file('version_manifest.json', 'https://piston-meta.mojang.com/mc/game/version_manifest.json')
    if status_code == 200:
        print("File downloaded successfully.")
    else:
        print("File download failed. Status code: ", status_code)
    version_manifest = load_json_file('version_manifest.json')
    return version_manifest

def get_lang_json(selected_version: str, version_json_url: str) -> dict | None:
    status_code = get_json_file(f'{selected_version}.json', version_json_url)
    if status_code == 200:
        print("File downloaded successfully.")
    else:
        print("File download failed. Status code: ", status_code)
        return
    version_json = load_json_file(f'{selected_version}.json')

    status_code = get_json_file(f'{version_json['assetIndex']['id']}.json', version_json['assetIndex']['url'])
    if status_code == 200:
        print("File downloaded successfully.")
    else:
        print("File download failed. Status code: ", status_code)
        return
    asset_index = load_json_file(f'{version_json["assetIndex"]["id"]}.json')
    
    status_code = get_json_file('zh_cn.json', f'https://resources.download.minecraft.net/{asset_index['objects']['minecraft/lang/zh_cn.json']['hash'][0:2]}/{asset_index['objects']['minecraft/lang/zh_cn.json']['hash']}')
    if status_code == 200:
        print("File downloaded successfully.")
    else:
        print("File download failed. Status code: ", status_code)
        return
    lang_json = load_json_file('zh_cn.json')
    return lang_json