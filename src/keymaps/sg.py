zhchsh: dict[str, str] = {
    'zh': 'v',
    'ch': 'i',
    'sh': 'u',
}

only_yunmu: dict[str, str] = {
    'ang': 'oh',
    'eng': 'og',
    'an': 'oj',
    'en': 'of',
    'ai': 'ol',
    'ei': 'oz',
    'ao': 'ok',
    'ou': 'ob',
    'er': 'or',
    'a': 'oa',
    'e': 'oe',
    'o': 'oo',
}
# 从长到短排序，确保优先匹配长的
only_yunmu_sorted: list[str] = sorted(only_yunmu, key=lambda x: -len(x))

end_yunmu: dict[str, str] = {
    'iang': 'd',
    'uang': 'd',
    'ang': 'h',

    'ian': 'm',
    'uan': 'r',
    'an': 'j',

    'ia': 'w',
    'ua': 'w',

    'uai': 'y',
    'ai': 'l',

    'ing': ';',
    'in': 'n',
    'un': 'p',

    'eng': 'g',
    'en': 'f',

    'ie': 'x',
    'ue': 't',

    'iong': 's',
    'ong': 's',

    'iao': 'c',
    'ao': 'k',
    'uo': 'o',

    'iu': 'q',
    'ou': 'b',

    'ei': 'z',
    'ui': 'v',

    'a': 'a',
    'e': 'e',
    'i': 'i',
    'o': 'o',
    'u': 'u',
}
# 从长到短排序，确保优先匹配长的
end_yunmu_sorted: list[str] = sorted(end_yunmu, key=lambda x: -len(x))

def to_sg(s: str) -> str:
    # 如果这个拼音只有韵母，则返回 only_yunmu 中的对应值
    for k in only_yunmu_sorted:
        if s == k:
            return only_yunmu[k]

    # 从长到短匹配韵母
    for k in end_yunmu_sorted:
        if s.find(k) != -1:
            s = s.replace(k, end_yunmu[k])
            break

    # 处理 zh ch sh
    for k, v in zhchsh.items():
        if s.startswith(k):
            s = s.replace(k, v)
            break

    return s
