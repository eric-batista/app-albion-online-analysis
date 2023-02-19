from devtools.providers.database import AsyncDatabaseProvider

from src.accounting.repositories import ItemRepository


class CreateNewItemUseCase:
    def __init__(self, default_database: AsyncDatabaseProvider):
        self._default_database = default_database.context()
        self._repository = ItemRepository(self._default_database)

    async def execute(self):
        pass


class UpdateItemUseCase:
    def __init__(self, default_database: AsyncDatabaseProvider):
        self._default_database = default_database.context()
        self._repository = ItemRepository(self._default_database)

    async def execute(self):
        pass


class ListItemsUseCase:
    def __init__(self, default_database: AsyncDatabaseProvider):
        self._default_database = default_database.context()
        self._repository = ItemRepository(self._default_database)

    async def execute(self):
        pass


class GetItemInfosUseCase:
    def __init__(self, default_database: AsyncDatabaseProvider):
        self._default_database = default_database.context()
        self._repository = ItemRepository(self._default_database)

    async def execute(self):
        pass
