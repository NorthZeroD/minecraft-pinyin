zhchsh: dict[str, str] = {
    "zh": "v",
    "ch": "u",
    "sh": "i",
}

only_yunmu: dict[str, str] = {
    "ang": "ag",
    "eng": "et",
    "an": "af",
    "en": "er",
    "ai": "as",
    "ei": "ew",
    "ao": "ad",
    "ou": "op",
    "er": "eq",
    "a": "aa",
    "e": "ee",
    "o": "oo",
}
# 从长到短排序，确保优先匹配长的
only_yunmu_sorted: list[str] = sorted(only_yunmu, key=lambda x: -len(x))

end_yunmu: dict[str, str] = {
    "iang": "h",
    "uang": "h",
    "ang": "g",
    "ian": "j",
    "uan": "c",
    "an": "f",
    "ia": "b",
    "ua": "b",
    "uai": "x",
    "ai": "s",
    "ing": "q",
    "in": "l",
    "un": "z",
    "eng": "t",
    "en": "r",
    "ie": "m",
    "ue": "x",
    "iong": "y",
    "ong": "y",
    "iao": "k",
    "ao": "d",
    "uo": "o",
    "iu": "n",
    "ou": "p",
    "ei": "w",
    "ui": "v",
    "a": "a",
    "e": "e",
    "i": "i",
    "o": "o",
    "u": "u",
}
# 从长到短排序，确保优先匹配长的
end_yunmu_sorted: list[str] = sorted(end_yunmu, key=lambda x: -len(x))


def to_jj(s: str) -> str:
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
