import re


def get_minecraft_versions(version_manifest_json: dict) -> list:
    minecraft_versions = []
    versions = version_manifest_json["versions"]
    for v in versions:
        minecraft_versions.append(v["id"])
    return minecraft_versions


def get_release_versions(minecraft_versions: list) -> list:
    release_versions = []
    for v in minecraft_versions:
        # 检查是否符合版本号格式（如 "x.y" 或 "x.y.z"）
        if re.match(r"^\d+\.\d+(\.\d+)?$", v):
            release_versions.append(v)
    return release_versions


def get_snapshot_versions(minecraft_versions: list) -> list:
    snapshot_versions = []
    for v in minecraft_versions:
        if not re.match(r"^\d+\.\d+(\.\d+)?$", v):
            snapshot_versions.append(v)
    return snapshot_versions


if __name__ == "__main__":
    from download import get_version_manifest_json

    version_manifest_json = get_version_manifest_json()
    minecraft_versions = get_minecraft_versions(version_manifest_json)
    release_versions = get_release_versions(minecraft_versions)
    snapshot_versions = get_snapshot_versions(minecraft_versions)
    print(snapshot_versions)
