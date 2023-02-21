from enum import Enum
from itertools import chain


class CitiesEnum(str, Enum):
    CAERLEON = "Caerleon"
    BRIDGEWATCH = "Bridgewatch"
    MARTLOCK = "Martlock"
    LYMHURST = "Lymhurst"
    FORT_STERLING = "Fort Sterling"
    THETFORD = "Thetford"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class RawItemsEnum(str, Enum):
    T2_ROCK = "T2_ROCK"
    T3_ROCK = "T3_ROCK"
    T4_ROCK = "T4_ROCK"
    T5_ROCK = "T5_ROCK"


class RefinedItemsEnum(str, Enum):
    T2_STONEBLOCK = "T2_STONEBLOCK"
    T3_STONEBLOCK = "T3_STONEBLOCK"
    T4_STONEBLOCK = "T4_STONEBLOCK"
    T5_STONEBLOCK = "T5_STONEBLOCK"


class ItemsEnum(str, Enum):
    _ignore_ = "member cls"
    cls = vars()
    for member in chain(list(RawItemsEnum), list(RefinedItemsEnum)):
        cls[member.name] = member.value
