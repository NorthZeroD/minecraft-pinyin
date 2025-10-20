zhchsh: dict[str, str] = {
    'zh': 'v',
    'ch': 'i',
    'sh': 'u',
}

only_yunmu: dict[str, str] = {
    'ang': 'ag',
    'eng': 'ah',
    'an': 'af',
    'en': 'ar',
    'ai': 'ak',
    'ei': 'ab',
    'ao': 'ac',
    'ou': 'ap',
    'er': 'al',
    'a': 'aa',
    'e': 'ae',
    'o': 'ao',
}
# 从长到短排序，确保优先匹配长的
only_yunmu_sorted: list[str] = sorted(only_yunmu, key=lambda x: -len(x))

end_yunmu: dict[str, str] = {
    'iang': 'n',
    'uang': 'n',
    'ang': 'g',

    'ian': 'd',
    'uan': 'w',
    'an': 'f',

    'ia': 'q',
    'ua': 'q',

    'uai': 'y',
    'ai': 'k',

    'ing': 'j',
    'in': 'l',
    'un': 'z',

    'eng': 'h',
    'en': 'r',

    'ie': 't',
    'ue': 'x',

    'iong': 's',
    'ong': 's',

    'iao': 'm',
    'ao': 'c',
    'uo': 'o',

    'iu': 'y',
    'ou': 'p',

    'ei': 'b',
    'ui': 'v',

    'a': 'a',
    'e': 'e',
    'i': 'i',
    'o': 'o',
    'u': 'u',
}
# 从长到短排序，确保优先匹配长的
end_yunmu_sorted: list[str] = sorted(end_yunmu, key=lambda x: -len(x))

def to_gb(s: str) -> str:
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
