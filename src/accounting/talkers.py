import aiohttp
from devtools.exceptions import NotFoundError

from src.core import settings


async def get_item_price_from_ao_prices_data(item_code: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{settings.BASE_AO_PRICES_DATA_API}/") as resp:
            response = await resp.json()
            if not resp.ok:
                raise NotFoundError("item")
            return response
