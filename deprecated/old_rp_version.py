def in_range(
    x: int, start: int, end: int, include_start: bool = True, include_end: bool = True
) -> bool:
    if include_start and include_end:
        return start >= x >= end
    elif include_start:
        return start >= x > end
    elif include_end:
        return start > x >= end
    else:
        return start > x > end


def get_rp_version(
    minecraft_versions: list[str], minecraft_version: str
) -> int | float:
    mvs = minecraft_versions
    mv = minecraft_version

    try:
        mv_index = mvs.index(mv)
    except ValueError:
        raise ValueError(
            f"Minecraft version '{mv}' not found in the provided version list"
        )

    if in_range(mv_index, mvs.index("13w24a"), mvs.index("1.8.9")):
        return 1
    elif in_range(mv_index, mvs.index("15w31a"), mvs.index("1.10.2")):
        return 2
    elif in_range(mv_index, mvs.index("16w32a"), mvs.index("17w47b")):
        return 3
    elif (
        in_range(mv_index, mvs.index("17w48a"), mvs.index("19w46b"))
        or mv == "3D Shareware v1.34"
    ):
        return 4
    elif (
        in_range(mv_index, mvs.index("1.15-pre1"), mvs.index("1.16.2-pre3"))
        or mv == "20w14infinite"
    ):
        return 5
    elif in_range(mv_index, mvs.index("1.16.2-rc1"), mvs.index("1.16.5")):
        return 6
    elif in_range(mv_index, mvs.index("20w45a"), mvs.index("21w38a")):
        return 7
    elif (
        in_range(mv_index, mvs.index("21w39a"), mvs.index("1.18.2"))
        or mv == "22w13oneblockatatime"
    ):
        return 8
    elif in_range(mv_index, mvs.index("22w11a"), mvs.index("1.19.2")):
        return 9
    elif in_range(mv_index, mvs.index("22w42a"), mvs.index("22w44a")):
        return 11
    elif in_range(mv_index, mvs.index("22w45a"), mvs.index("23w07a")):
        return 12
    elif (
        in_range(mv_index, mvs.index("1.19.4-pre1"), mvs.index("23w13a"))
        or mv == "23w13a_or_b"
    ):
        return 13
    elif in_range(mv_index, mvs.index("23w14a"), mvs.index("23w16a")):
        return 14
    elif in_range(mv_index, mvs.index("23w17a"), mvs.index("1.20.1")):
        return 15
    elif in_range(mv_index, mvs.index("23w31a"), mvs.index("23w31a")):
        return 16
    elif in_range(mv_index, mvs.index("23w32a"), mvs.index("1.20.2-pre1")):
        return 17
    elif in_range(mv_index, mvs.index("1.20.2-pre2"), mvs.index("23w41a")):
        return 18
    elif in_range(mv_index, mvs.index("23w42a"), mvs.index("23w42a")):
        return 19
    elif in_range(mv_index, mvs.index("23w43a"), mvs.index("23w44a")):
        return 20
    elif in_range(mv_index, mvs.index("23w45a"), mvs.index("23w46a")):
        return 21
    elif in_range(mv_index, mvs.index("1.20.3-pre1"), mvs.index("23w51b")):
        return 22
    elif in_range(mv_index, mvs.index("24w03a"), mvs.index("24w04a")):
        return 24
    elif in_range(mv_index, mvs.index("24w05a"), mvs.index("24w05b")):
        return 25
    elif in_range(mv_index, mvs.index("24w06a"), mvs.index("24w07a")):
        return 26
    elif in_range(mv_index, mvs.index("24w09a"), mvs.index("24w10a")):
        return 28
    elif in_range(mv_index, mvs.index("24w11a"), mvs.index("24w11a")):
        return 29
    elif (
        in_range(mv_index, mvs.index("24w12a"), mvs.index("24w12a"))
        or mv == "24w14potato"
    ):
        return 30
    elif in_range(mv_index, mvs.index("24w13a"), mvs.index("1.20.5-pre3")):
        return 31
    elif in_range(mv_index, mvs.index("1.20.5-pre4"), mvs.index("1.20.6")):
        return 32
    elif in_range(mv_index, mvs.index("24w18a"), mvs.index("24w20a")):
        return 33
    elif in_range(mv_index, mvs.index("24w21a"), mvs.index("1.21.1")):
        return 34
    elif in_range(mv_index, mvs.index("24w33a"), mvs.index("24w33a")):
        return 35
    elif in_range(mv_index, mvs.index("24w34a"), mvs.index("24w35a")):
        return 36
    elif in_range(mv_index, mvs.index("24w36a"), mvs.index("24w36a")):
        return 37
    elif in_range(mv_index, mvs.index("24w37a"), mvs.index("24w37a")):
        return 38
    elif in_range(mv_index, mvs.index("24w38a"), mvs.index("24w39a")):
        return 39
    elif in_range(mv_index, mvs.index("24w40a"), mvs.index("24w40a")):
        return 40
    elif in_range(mv_index, mvs.index("1.21.2-pre1"), mvs.index("1.21.2-pre2")):
        return 41
    elif in_range(mv_index, mvs.index("1.21.2-pre3"), mvs.index("1.21.3")):
        return 42
    elif in_range(mv_index, mvs.index("24w44a"), mvs.index("24w44a")):
        return 43
    elif in_range(mv_index, mvs.index("24w45a"), mvs.index("24w45a")):
        return 44
    elif in_range(mv_index, mvs.index("24w46a"), mvs.index("24w46a")):
        return 45
    elif in_range(mv_index, mvs.index("1.21.4-pre1"), mvs.index("1.21.4")):
        return 46
    elif in_range(mv_index, mvs.index("25w02a"), mvs.index("25w02a")):
        return 47
    elif in_range(mv_index, mvs.index("25w03a"), mvs.index("25w03a")):
        return 48
    elif in_range(mv_index, mvs.index("25w04a"), mvs.index("25w04a")):
        return 49
    elif in_range(mv_index, mvs.index("25w05a"), mvs.index("25w05a")):
        return 50
    elif in_range(mv_index, mvs.index("25w06a"), mvs.index("25w06a")):
        return 51
    elif in_range(mv_index, mvs.index("25w07a"), mvs.index("25w07a")):
        return 52
    elif in_range(mv_index, mvs.index("25w08a"), mvs.index("25w09b")):
        return 53
    elif in_range(mv_index, mvs.index("25w10a"), mvs.index("25w10a")):
        return 54
    elif (
        in_range(mv_index, mvs.index("1.21.5-pre1"), mvs.index("1.21.5"))
        or mv == "25w14craftmine"
    ):
        return 55
    elif in_range(mv_index, mvs.index("25w15a"), mvs.index("25w15a")):
        return 56
    elif in_range(mv_index, mvs.index("25w16a"), mvs.index("25w16a")):
        return 57
    elif in_range(mv_index, mvs.index("25w17a"), mvs.index("25w17a")):
        return 58
    elif in_range(mv_index, mvs.index("25w18a"), mvs.index("25w18a")):
        return 59
    elif in_range(mv_index, mvs.index("25w19a"), mvs.index("25w19a")):
        return 60
    elif in_range(mv_index, mvs.index("25w20a"), mvs.index("25w20a")):
        return 61
    elif in_range(mv_index, mvs.index("25w21a"), mvs.index("25w21a")):
        return 62
    elif in_range(mv_index, mvs.index("1.21.6-pre1"), mvs.index("1.21.7-rc1")):
        return 63
    elif in_range(mv_index, mvs.index("1.21.7-rc2"), mvs.index("1.21.8")):
        return 64
    elif in_range(mv_index, mvs.index("25w31a"), mvs.index("25w31a")):
        return 65.0
    elif in_range(mv_index, mvs.index("25w32a"), mvs.index("25w32a")):
        return 65.1
    elif in_range(mv_index, mvs.index("25w33a"), mvs.index("25w33a")):
        return 65.2
    elif in_range(mv_index, mvs.index("25w34a"), mvs.index("25w34b")):
        return 66.0
    elif in_range(mv_index, mvs.index("25w35a"), mvs.index("25w35a")):
        return 67.0
    elif in_range(mv_index, mvs.index("25w36a"), mvs.index("25w36b")):
        return 68.0
    elif in_range(mv_index, mvs.index("25w37a"), mvs.index("1.21.10")):
        return 69.0
    elif in_range(mv_index, mvs.index("25w41a"), mvs.index("25w41a")):
        return 70.0
    elif in_range(mv_index, mvs.index("25w42a"), mvs.index("25w42a")):
        return 70.1
    elif in_range(mv_index, mvs.index("25w43a"), mvs.index("25w43a")):
        return 71.0
    elif in_range(mv_index, mvs.index("25w44a"), mvs.index("25w44a")):
        return 72.0
    else:
        raise ValueError(
            f"Minecraft version '{mv}' does not match any known resource pack version range"
        )
