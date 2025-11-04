from rp_versions import rp_versions

pack_meta_new = {
    "pack": {
        "description": "Pinyin Resource Pack\nNorthZeroD/minecraft-pinyin",
        "min_format": 0,
        "max_format": 0,
    }
}

pack_meta_old = {
    "pack": {
        "description": "Pinyin Resource Pack\nNorthZeroD/minecraft-pinyin",
        "pack_format": 0,
    }
}


def get_pack_meta(
    minecraft_version: str,
    description: str,
    minecraft_versions: list,
) -> dict:
    index_current = minecraft_versions.index(minecraft_version)
    # 版本小于(索引大于) 23w31a 使用 pack_meta_old
    index_23w31a = minecraft_versions.index("23w31a")
    if index_current > index_23w31a:
        pack_meta = pack_meta_old
        v = rp_versions[minecraft_version]
        pack_meta["pack"]["pack_format"] = int(float(v))
    else:
        pack_meta = pack_meta_new
        v = rp_versions[minecraft_version]
        pack_meta["pack"]["min_format"] = int(float(v))
        pack_meta["pack"]["max_format"] = int(float(v))
    pack_meta["pack"]["description"] = description
    return pack_meta
