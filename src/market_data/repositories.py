import contextlib
from datetime import datetime
from typing import List
from uuid import uuid4

from devtools.providers.database.asyncio import (AsyncContext,
                                                 AsyncDatabaseProvider)
from devtools.providers.database.filters import And, Field, Filter, OrderBy
from devtools.providers.database.helpers.async_ import AsyncRepository

from src.market_data.entities import ItemsHistory
from src.market_data.models import (GatheringItems, ItemCreate,
                                    ItemCreateRequest, ItemModel)


class ItemsHistoryRepository:
    def __init__(self, context: AsyncContext):
        self._context = context
        self._repo = AsyncRepository(ItemsHistory, ItemModel)

    @classmethod
    def from_provider(cls, provider: AsyncDatabaseProvider):
        return cls(provider.context())

    async def create(self, item: ItemCreateRequest):
        # with contextlib.suppress(Exception):
        #     return await self.get(item=item)

        new_item = ItemCreate(id=uuid4(), created_at=datetime.now(), **item.dict())
        if new_item.last_buy_price == 0 and new_item.last_sell_price == 0:
            return
        result = await self._repo.create(context=self._context, payload=new_item)
        return result.get()

    async def delete(self, item: ItemCreateRequest):
        clause = And(Field("name", item.name), Field("city", item.city))
        await self._repo.delete(context=self._context, clause=clause)

    async def update(self):
        return

    async def get(self, item: ItemCreateRequest | GatheringItems) -> List[ItemModel]:
        clause = And(Field("name", item.name), Field("city", item.city))
        result = await self._repo.get(context=self._context, clause=clause)
        return [result.get()]

    async def get_all(self):
        result = await self._repo.search(context=self._context)
        return result.get()

    async def get_all_by_item(self, item: GatheringItems | ItemCreateRequest):
        result = await self._repo.search(
            self._context,
            Field("name", item.name),
            Field("city", item.city),
            order_by=OrderBy("created_at", order="desc"),
        )
        return result.get()
