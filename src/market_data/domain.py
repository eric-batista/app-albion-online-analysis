from datetime import datetime
from typing import List

from devtools.providers.database import AsyncDatabaseProvider

from src.market_data import models
from src.market_data.repositories import ItemsHistoryRepository
from src.market_data.talkers import get_item_price_from_ao_prices_data
from src.utils.enums import ItemsEnum
from src.utils.models import AlbionOnlineDataResponse


class GetItemsInfosFromAOData:
    def __init__(
        self, payload: models.ItemsListRequest, default_database: AsyncDatabaseProvider
    ):
        self._items = payload
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def create_new_item_history(self, item: models.ItemCreateRequest):
        return await self._repository.create(item=item)

    async def execute(self):
        ao_data_response = await get_item_price_from_ao_prices_data(self._items)
        return [
            await self.create_new_item_history(
                models.ItemCreateRequest(
                    name=item.item_id,
                    city=item.city,  # type: ignore
                    last_buy_price=item.buy_price_min,
                    last_sell_price=item.sell_price_min,
                    last_price_date=datetime.now(),
                )
            )
            for item in ao_data_response
        ]


class GetBestPlaceToSellItem:
    def __init__(self, item_id: str, default_database: AsyncDatabaseProvider):
        self._item_id = item_id
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def _get_item_info(self):
        return await get_item_price_from_ao_prices_data(self._item_id)

    def _get_highest_sell_price(self, item_info: List[AlbionOnlineDataResponse]):
        return max(item_info, key=lambda x: x.buy_price_max)

    async def execute(self):
        item_info = await self._get_item_info()
        return self._get_highest_sell_price(item_info)


class ListItemsInfosHistory:
    def __init__(self, default_database: AsyncDatabaseProvider):
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def list_items_history(self):
        return await self._repository.get_all()

    async def execute(self):
        return await self.list_items_history()


class CalculateGatheringProfit:
    def __init__(
        self,
        payload: models.CalculateGatheringRequest,
        default_database: AsyncDatabaseProvider,
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def _get_item_price(self, item: models.GatheringItems) -> models.ItemModel:
        items = await self._repository.get_all_by_item(item)
        return items[0]

    async def _calculate_item_profit(
        self, item_info: models.ItemModel, item: models.GatheringItems
    ):
        total = item_info.last_sell_price * item.quantity
        taxes = total * 0.08
        return total - taxes

    async def execute(self):
        response_infos = []
        for item in self._payload.data:
            item_info = await self._get_item_price(item=item)
            profit = await self._calculate_item_profit(item_info, item)

            response_infos.append(GatheringItemsProfit(profit=profit, **item.dict()))  # type: ignore

        return {"data": response_infos}


class CalculateDiaryProfit:
    def __init__(
        self,
        default_database: AsyncDatabaseProvider,
        payload: models.CalculateGatheringRequest | None = None,
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def execute(self):
        return


class UpdateAllItemsPrices:
    def __init__(
        self,
        payload: models.CalculateGatheringRequest | None,
        default_database: AsyncDatabaseProvider,
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def _update_item_price(self, item_info):
        return  # self._repository.update(item_info)

    async def execute(self):
        if not self._payload:
            items = ItemsEnum.list()
            ao_data_request = models.ItemsListRequest.parse_obj(items)
            ao_data_response = await get_item_price_from_ao_prices_data(ao_data_request)
            for item_info in ao_data_response:
                await self._update_item_price(item_info)
            return

        for item in self._payload.data:
            ao_data_response = await get_item_price_from_ao_prices_data(item)  # type: ignore
            await self._update_item_price(ao_data_response)
        return
