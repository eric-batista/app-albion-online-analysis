from uuid import uuid4

from devtools.providers.database.asyncio import (AsyncContext,
                                                 AsyncDatabaseProvider)
from devtools.providers.database.helpers.async_ import AsyncRepository

from src.player_stats import entities, models


class PlayerStatsRepository:
    def __init__(self, context: AsyncContext) -> None:
        self._context = context
        self._repo = AsyncRepository(entities.PlayerStats, models.PlayerStatsModel)

    @classmethod
    def from_provider(cls, provider: AsyncDatabaseProvider):
        return cls(provider.context())

    async def create(
        self, player_info: models.PlayerStatsPayload
    ) -> models.PlayerStatsModel:
        player = models.PlayerStatsCreate(id=uuid4(), name=player_info.name)
        result = await self._repo.create(context=self._context, payload=player)
        return result.get()


class CombatStatsRepository:
    def __init__(self, context: AsyncContext) -> None:
        self._context = context
        self._repo = AsyncRepository(entities.CombatStats, models.CombatStatsModel)
        self._spec_repo = AsyncRepository(
            entities.CombatSpecialist, models.CombatStatsModel
        )

    async def create(
        self, combat_info: models.CombatStatsCreate
    ) -> models.CombatStatsModel:
        combat_stats = models.CombatStatsCreate(
            id=uuid4(),
            name=combat_info.name,
            level=combat_info.level,
            max_tier_enable=combat_info.max_tier_enable,
        )
        result = await self._repo.create(context=self._context, payload=combat_stats)
        return result.get()


class FarmingStatsRepository:
    def __init__(self, context: AsyncContext) -> None:
        self._context = context
