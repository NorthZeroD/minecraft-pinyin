pack_meta_new = {
    "pack": {
        "description": "Pinyin Resource Pack\nNorthZeroD/minecraft-pinyin",
        "min_format": 65,
        "max_format": 99,
    }
}

pack_meta_old = {
    "pack": {
        "description": "Pinyin Resource Pack\nNorthZeroD/minecraft-pinyin",
        "pack_format": 4,
        "supported_formats": [4, 64],
    }
}


def get_pack_meta(
    minecraft_version: str,
    description: str,
    minecraft_versions: list,
) -> dict:
    index_current = minecraft_versions.index(minecraft_version)
    # 版本小于(索引大于) 25w31a 使用 pack_meta_old
    index_25w31a = minecraft_versions.index("25w31a")
    if index_current > index_25w31a:
        pack_meta = pack_meta_old
    else:
        pack_meta = pack_meta_new
    pack_meta["pack"]["description"] = description
    return pack_meta
