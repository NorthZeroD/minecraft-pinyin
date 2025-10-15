zhchsh = {
    'zh': 'v',
    'ch': 'i',
    'sh': 'u',
}
xiaohe_keymap = {
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
xiaohe_keymap_sorted = sorted(xiaohe_keymap, key=lambda x: -len(x))

def to_xiaohe(s: str) -> str:
    # 只有一个单韵母，那么就双写
    if len(s) == 1:
        return s * 2

    # 从长到短匹配韵母
    for k in xiaohe_keymap_sorted:
        if s.find(k) != -1:
            s = s.replace(k, xiaohe_keymap[k])
            break

    # 处理 zh ch sh
    for k, v in zhchsh.items():
        if s.startswith(k):
            s = s.replace(k, v)
            break

    return s
