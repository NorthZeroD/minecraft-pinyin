zhchsh: dict[str, str] = {
    'zh': 'v',
    'ch': 'i',
    'sh': 'u',
}

only_yunmu: dict[str, str] = {
    'ang': 'ah',
    'eng': 'eg',
    'an': 'an',
    'en': 'en',
    'ai': 'ai',
    'ei': 'ei',
    'ao': 'ao',
    'ou': 'ou',
    'er': 'er',
    'a': 'aa',
    'e': 'ee',
    'o': 'oo',
}
# 从长到短排序，确保优先匹配长的
only_yunmu_sorted: list[str] = sorted(only_yunmu, key=lambda x: -len(x))

end_yunmu: dict[str, str] = {
    'iang': 'l',
    'uang': 'l',
    'ang': 'h',

    'ian': 'm',
    'uan': 'r',
    'an': 'j',
    
    'ia': 'x',
    'ua': 'x',
    
    'uai': 'k',
    'ai': 'd',
    
    'ing': 'k',
    'in': 'b',
    'un': 'y',
    
    'eng': 'g',
    'en': 'f',
    
    'ie': 'p',
    'ue': 't',
    
    'iong': 's',
    'ong': 's',
    
    'iao': 'n',
    'ao': 'c',
    'uo': 'o',
    
    'iu': 'q',
    'ou': 'z',
    
    'ei': 'w',
    'ui': 'v',
    
    'a': 'a',
    'e': 'e',
    'i': 'i',
    'o': 'o',
    'u': 'u',
}
# 从长到短排序，确保优先匹配长的
end_yunmu_sorted: list[str] = sorted(end_yunmu, key=lambda x: -len(x))

def to_xh(s: str) -> str:
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
