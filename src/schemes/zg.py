zhchsh: dict[str, str] = {
    "zh": "u",
    "ch": "a",
    "sh": "i",
}

only_yunmu: dict[str, str] = {
    "ang": "os",
    "eng": "ot",
    "an": "or",
    "en": "ow",
    "ai": "op",
    "ei": "ok",
    "ao": "oq",
    "ou": "oz",
    "er": "oj",
    "a": "oa",
    "e": "oe",
    "o": "oo",
}
# 从长到短排序，确保优先匹配长的
only_yunmu_sorted: list[str] = sorted(only_yunmu, key=lambda x: -len(x))

end_yunmu: dict[str, str] = {
    "iang": "g",
    "uang": "g",
    "ang": "s",
    "ian": "f",
    "uan": "l",
    "an": "r",
    "ia": "x",
    "ua": "x",
    "uai": "y",
    "ai": "p",
    "ing": ";",
    "in": "y",
    "un": "m",
    "eng": "t",
    "en": "w",
    "ie": "d",
    "ue": "n",
    "iong": "h",
    "ong": "h",
    "iao": "b",
    "ao": "q",
    "uo": "o",
    "iu": "j",
    "ou": "z",
    "ei": "k",
    "ui": "n",
    "a": "a",
    "e": "e",
    "i": "i",
    "o": "o",
    "u": "u",
}
# 从长到短排序，确保优先匹配长的
end_yunmu_sorted: list[str] = sorted(end_yunmu, key=lambda x: -len(x))


def to_zg(s: str) -> str:
    # 如果这个拼音只有韵母，则返回 only_yunmu 中的对应值
    for k in only_yunmu_sorted:
        if s == k:
            return only_yunmu[k]
    # 处理 zh ch sh
    for k, v in zhchsh.items():
        if s.startswith(k):
            s = s.replace(k, v)
            break
    # 从长到短匹配韵母
    for k in end_yunmu_sorted:
        if s.find(k) != -1:
            s = s.replace(k, end_yunmu[k])
            break
    return s
