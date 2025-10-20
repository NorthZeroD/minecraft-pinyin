from pypinyin import lazy_pinyin, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict
from schemes.xh import to_xh
from schemes.zrm import to_zrm
from schemes.sg import to_sg
from schemes.wr import to_wr
from schemes.zg import to_zg
from schemes.abc import to_abc
from schemes.gb import to_gb
from schemes.jj import to_jj


def szm(pinyin_list: list) -> str:
    l = [(lambda x: x[0])(i) for i in pinyin_list]
    s = "".join(l)
    return s


def qp(pinyin_list: list) -> str:
    s = "".join(pinyin_list)
    return s


def xh(pinyin_list: list) -> str:
    l = [to_xh(i) for i in pinyin_list]
    s = "".join(l)
    return s


def zrm(pinyin_list: list) -> str:
    l = [to_zrm(i) for i in pinyin_list]
    s = "".join(l)
    return s


def sg(pinyin_list: list) -> str:
    l = [to_sg(i) for i in pinyin_list]
    s = "".join(l)
    return s


def wr(pinyin_list: list) -> str:
    l = [to_wr(i) for i in pinyin_list]
    s = "".join(l)
    return s


def zg(pinyin_list: list) -> str:
    l = [to_zg(i) for i in pinyin_list]
    s = "".join(l)
    return s


def abc(pinyin_list: list) -> str:
    l = [to_abc(i) for i in pinyin_list]
    s = "".join(l)
    return s


def gb(pinyin_list: list) -> str:
    l = [to_gb(i) for i in pinyin_list]
    s = "".join(l)
    return s


def jj(pinyin_list: list) -> str:
    l = [to_jj(i) for i in pinyin_list]
    s = "".join(l)
    return s


if __name__ == "__main__":
    cc_cedict.load()
    load_phrases_dict(phrases_dict)
    l = lazy_pinyin("快乐恶魂刷怪蛋", errors="exception")
    print(sg(l))
