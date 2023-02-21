from typing import List

import aiohttp
from devtools.exceptions import NotFoundError

from src.accounting.models import ItemsListRequest
from src.core import settings
from src.utils.helpers import filter_cities
from src.utils.models import AlbionOnlineDataResponse


async def get_item_price_from_ao_prices_data(
    items_code: ItemsListRequest, location: str | None = None
) -> List[AlbionOnlineDataResponse]:
    splited_items = ",".join(items_code.items)
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{settings.BASE_AO_PRICES_DATA_API}/{splited_items}.json?locations={location}"
        ) as resp:
            response = await resp.json()
            if not resp.ok:
                raise NotFoundError("items")
            return filter_cities(
                [AlbionOnlineDataResponse.parse_obj(item) for item in response]
            )
