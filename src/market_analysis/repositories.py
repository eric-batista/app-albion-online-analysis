from datetime import datetime
from typing import List
from uuid import uuid4

from devtools.providers.database.asyncio import (AsyncContext,
                                                 AsyncDatabaseProvider)
from devtools.providers.database.filters import And, Field, Filter, OrderBy
from devtools.providers.database.helpers.async_ import AsyncRepository

from src.market_analysis import entities, models


class ExpectedProfitRepository:
    def __init__(self, context: AsyncContext):
        self._context = context
        self._repo = AsyncRepository(
            entities.ExpectedProfitHistory, models.ExpectedProfitHistory
        )

    @classmethod
    def from_provider(cls, provider: AsyncDatabaseProvider):
        return cls(provider.context())

    async def create(self, expected_profit):
        new_item = models.ExpectedProfitHistoryCreate(
            id=uuid4(), created_at=datetime.now(), **expected_profit.dict()
        )
        result = await self._repo.create(context=self._context, payload=new_item)
        return result.get()
