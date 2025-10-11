from download import *
from utils import *

def main() -> None:
    version_manifest = get_version_manifest()

    print(version_manifest['latest'])
    selected_version: str = input("Enter the Minecraft version: ")
    for v in version_manifest['versions']:
        if v['id'] == selected_version:
            version_json_url = v['url']
            break
    else:
        print("Version not found.")
        return
    
    lang_json = get_lang_json(selected_version, version_json_url)
    if lang_json is None:
        print("Failed to get language JSON.")
        return

if __name__ == "__main__":
    main()
