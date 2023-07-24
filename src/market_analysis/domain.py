from devtools.providers.database import AsyncDatabaseProvider

import src.market_data.models as market_models
from src.market_analysis.repositories import ExpectedProfitRepository
from src.market_data.talkers import get_item_price_from_ao_prices_data


class GenerateMarketDataFromTimeSeries:
    pass


class GenerateSVMModelFromTimeSeries:
    pass


class GetExpectedProfitByLocation:
    def __init__(
        self,
        items: market_models.ItemsListRequest,
        save_registry: bool,
        default_database: AsyncDatabaseProvider,
    ):
        self._items = items
        self._default_database = default_database.context()
        self._repository = ExpectedProfitRepository(self._default_database)
        self._save_registry = save_registry

    async def _calculate_expected_profit_by_location(self, items_info):
        return

    async def _save_profit_registry(self, expected_profit):
        return await self._repository.create(expected_profit)

    async def execute(self):
        items_info = await get_item_price_from_ao_prices_data(self._items)

        expected_profit = await self._calculate_expected_profit_by_location(items_info)
        if self._save_registry:
            await self._save_profit_registry(expected_profit)
        return
