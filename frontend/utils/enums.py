from enum import Enum, unique

class BaseEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


@unique
class ItemsEnum(str, BaseEnum):
    T2_ROCK = "T2_ROCK"
    T3_ROCK = "T3_ROCK"
    T4_ROCK = "T4_ROCK"
    T5_ROCK = "T5_ROCK"


@unique
class CitiesEnum(str, BaseEnum):
    CAERLEON = "Caerleon"
    BRIDGEWATCH = "Bridgewatch"
    MARTLOCK = "Martlock"
    LYMHURST = "Lymhurst"
    FORT_STERLING = "Fort Sterling"
    THETFORD = "Thetford"
