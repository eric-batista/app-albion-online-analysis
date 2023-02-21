from datetime import datetime
from typing import List
from uuid import UUID

from devtools.providers.database import AsyncDatabaseProvider

from src.accounting.models import ItemCreateRequest
from src.accounting.repositories import ItemsHistoryRepository
from src.accounting.talkers import get_item_price_from_ao_prices_data
from src.utils.enums import ItemsEnum


class GetItemsInfosUseCase:
    def __init__(self, items: List[ItemsEnum], default_database: AsyncDatabaseProvider):
        self._items = items
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def create_new_item_history(self, item: ItemCreateRequest):
        return await self._repository.create(item=item)

    async def execute(self):
        ao_data_response = await get_item_price_from_ao_prices_data(self._items)
        return [
            await self.create_new_item_history(
                ItemCreateRequest(
                    name=item.item_id,
                    city=item.city,
                    last_buy_price=item.buy_price_min,
                    last_sell_price=item.sell_price_min,
                    last_price_date=datetime.now(),
                )
            )
            for item in ao_data_response
        ]
