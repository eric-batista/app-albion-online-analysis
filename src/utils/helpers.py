from typing import List

from .enums import CitiesEnum
from .models import AlbionOnlineDataResponse


def filter_cities(response: List[AlbionOnlineDataResponse]):
    return [infos for infos in response if CitiesEnum.has_value(infos.city)]
