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


format_converters = {
    "src": "src",
    "szm": szm,
    "qp": qp,
    "xh": xh,
    "zrm": zrm,
    "sg": sg,
    "wr": wr,
    "zg": zg,
    "abc": abc,
    "gb": gb,
    "jj": jj,
    "none": "none",
}
