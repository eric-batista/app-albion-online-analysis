from datetime import datetime
from uuid import uuid4

from devtools.providers.database.asyncio import (AsyncContext,
                                                 AsyncDatabaseProvider)
from devtools.providers.database.helpers.async_ import AsyncRepository

from src.accounting.entities import ItemsHistoryEntity
from src.accounting.models import ItemCreate, ItemCreateRequest, ItemModel


class ItemsHistoryRepository:
    def __init__(self, context: AsyncContext):
        self._context = context
        self._repo = AsyncRepository(ItemsHistoryEntity, ItemModel)

    @classmethod
    def from_provider(cls, provider: AsyncDatabaseProvider):
        return cls(provider.context())

    async def create(self, item: ItemCreateRequest):
        new_item = ItemCreate(id=uuid4(), created_at=datetime.now(), **item.dict())
        result = await self._repo.create(context=self._context, payload=new_item)
        return result.get()

    async def delete(self):
        return

    async def update(self):
        return
