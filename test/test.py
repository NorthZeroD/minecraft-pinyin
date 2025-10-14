def func1():
    from pypinyin import pinyin
    print(pinyin('枯萎'))

def func2():
    from pypinyin import pinyin
    from pypinyin_dict.phrase_pinyin_data import cc_cedict
    cc_cedict.load()
    print(pinyin('枯萎'))

if __name__ == '__main__':
    func1()
    func2()
