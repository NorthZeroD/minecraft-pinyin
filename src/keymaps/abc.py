zhchsh: dict[str, str] = {
    'zh': 'a',
    'ch': 'e',
    'sh': 'v',
}

only_yunmu: dict[str, str] = {
    'ang': 'oh',
    'eng': 'og',
    'an': 'oj',
    'en': 'of',
    'ai': 'ol',
    'ei': 'oq',
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
    'iang': 't',
    'uang': 't',
    'ang': 'h',

    'ian': 'w',
    'uan': 'p',
    'an': 'j',

    'ia': 'd',
    'ua': 'd',

    'uai': 'c',
    'ai': 'l',

    'ing': 'y',
    'in': 'c',
    'un': 'n',

    'eng': 'g',
    'en': 'f',

    'ie': 'x',
    'ue': 'm',

    'iong': 's',
    'ong': 's',

    'iao': 'z',
    'ao': 'k',
    'uo': 'o',

    'iu': 'r',
    'ou': 'b',

    'ei': 'q',
    'ui': 'm',

    'a': 'a',
    'e': 'e',
    'i': 'i',
    'o': 'o',
    'u': 'u',
}
# 从长到短排序，确保优先匹配长的
end_yunmu_sorted: list[str] = sorted(end_yunmu, key=lambda x: -len(x))

def to_abc(s: str) -> str:
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
