from enum import Enum
from itertools import chain


class ItemTier(str, Enum):
    TIER_1 = "T1"
    TIER_2 = "T2"
    TIER_3 = "T3"
    TIER_4 = "T4"
    TIER_5 = "T5"
    TIER_6 = "T6"
    TIER_7 = "T7"
    TIER_8 = "T8"


class ItemQuality(Enum):
    pass


class ItemEnchantment(Enum):
    pass


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
    T2_ORE = "T2_ORE"
    T3_ORE = "T3_ORE"
    T4_ORE = "T4_ORE"
    T5_ORE = "T5_ORE"
    T2_WOOD = "T2_WOOD"
    T3_WOOD = "T3_WOOD"
    T4_WOOD = "T4_WOOD"
    T5_WOOD = "T5_WOOD"
    T2_FIBER = "T2_FIBER"
    T3_FIBER = "T3_FIBER"
    T4_FIBER = "T4_FIBER"
    T5_FIBER = "T5_FIBER"
    T2_HIDE = "T2_HIDE"
    T3_HIDE = "T3_HIDE"
    T4_HIDE = "T4_HIDE"
    T5_HIDE = "T5_FIBER"


class RefinedItemsEnum(str, Enum):
    T2_STONEBLOCK = "T2_STONEBLOCK"
    T3_STONEBLOCK = "T3_STONEBLOCK"
    T4_STONEBLOCK = "T4_STONEBLOCK"
    T5_STONEBLOCK = "T5_STONEBLOCK"
    T2_CLOTH = "T2_CLOTH"
    T3_CLOTH = "T3_CLOTH"
    T4_CLOTH = "T4_CLOTH"
    T5_CLOTH = "T5_CLOTH"
    T2_LEATHER = "T2_LEATHER"
    T3_LEATHER = "T3_LEATHER"
    T4_LEATHER = "T4_LEATHER"
    T5_LEATHER = "T5_LEATHER"
    T2_METALBAR = "T2_METALBAR"
    T3_METALBAR = "T3_METALBAR"
    T4_METALBAR = "T4_METALBAR"
    T5_METALBAR = "T5_METALBAR"
    T2_PLANKS = "T2_PLANKS"
    T3_PLANKS = "T3_PLANKS"
    T4_PLANKS = "T4_PLANKS"
    T5_PLANKS = "T5_PLANKS"


class ItemsEnum(str, Enum):
    _ignore_ = "member cls"
    cls = vars()
    for member in chain(list(RawItemsEnum), list(RefinedItemsEnum)):
        cls[member.name] = member.value  # type: ignore

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
