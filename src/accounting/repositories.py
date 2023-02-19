from devtools.providers.database.asyncio import (AsyncContext,
                                                 AsyncDatabaseProvider)
from devtools.providers.database.helpers.async_ import AsyncRepository

from src.accounting.entities import ItemEntity
from src.accounting.models import ItemModel


class ItemRepository:
    def __init__(self, context: AsyncContext):
        self._context = context
        self._repo = AsyncRepository(ItemEntity, ItemModel)

    @classmethod
    def from_provider(cls, provider: AsyncDatabaseProvider):
        return cls(provider.context())

    async def create(self):
        return

    async def delete(self):
        return

    async def update(self):
        return
