from datetime import datetime
from typing import List

from devtools.providers.database import AsyncDatabaseProvider

from src.player_stats import models
from src.player_stats.repositories import PlayerStatsRepository


class CreatePlayerStats:
    def __init__(
        self,
        payload: models.PlayerStatsPayload,
        default_database: AsyncDatabaseProvider,
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = PlayerStatsRepository(self._default_database)

    async def _create_player_stats(self):
        return await self._repository.create(player_info=self._payload)

    async def execute(self):
        try:
            player_stats = await self._create_player_stats()
        except Exception as e:
            raise e
        return player_stats


class UpdatePlayerStats:
    def __init__(
        self, payload: models.PlayerStatsCreate, default_database: AsyncDatabaseProvider
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = PlayerStatsRepository(self._default_database)


class DeletePlayerStats:
    def __init__(
        self, payload: models.PlayerStatsCreate, default_database: AsyncDatabaseProvider
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = PlayerStatsRepository(self._default_database)


class GetPlayerStats:
    pass


class ListAllPlayersStats:
    pass
