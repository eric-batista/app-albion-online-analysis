from datetime import datetime
from typing import List

from devtools.providers.database import AsyncDatabaseProvider

from src.accounting.models import (CalculateGatheringRequest, GatheringItems,
                                   GatheringItemsProfit, ItemCreateRequest,
                                   ItemModel, ItemsListRequest)
from src.accounting.repositories import ItemsHistoryRepository
from src.accounting.talkers import get_item_price_from_ao_prices_data
from src.utils.enums import ItemsEnum


class GetItemsInfosFromAoDataUseCase:
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


class ListItemsInfosHistoryUseCase:
    def __init__(self, default_database: AsyncDatabaseProvider):
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def list_items_history(self):
        return await self._repository.get_all()

    async def execute(self):
        return await self.list_items_history()


class CalculateGatheringProfitUseCase:
    def __init__(
        self,
        payload: CalculateGatheringRequest,
        default_database: AsyncDatabaseProvider,
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)

    async def _get_item_price(self, item: GatheringItems) -> ItemModel:
        items = await self._repository.get_all_by_item(item)
        return items[0]

    async def _calculate_item_profit(self, item_info: ItemModel, item: GatheringItems):
        total = item_info.last_sell_price * item.quantity
        taxes = total * 0.08
        return int(total - taxes)

    async def execute(self):
        response_infos = []
        for item in self._payload.data:
            item_info = await self._get_item_price(item=item)
            profit = await self._calculate_item_profit(item_info, item)

            response_infos.append(GatheringItemsProfit(profit=profit, **item.dict()))

        return {"data": response_infos}


class CalculateDiaryProfitUseCase:
    def __init__(
        self,
        payload: CalculateGatheringRequest | None,
        default_database: AsyncDatabaseProvider,
    ):
        self._payload = payload
        self._default_database = default_database.context()
        self._repository = ItemsHistoryRepository(self._default_database)


    async def execute(self):

        return


class UpdateAllItemsPricesUseCase:
    def __init__(
        self,
        payload: CalculateGatheringRequest | None,
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
            ao_data_request = ItemsListRequest(items=items)
            ao_data_response = await get_item_price_from_ao_prices_data(ao_data_request)
            for item_info in ao_data_response:
                await self._update_item_price(item_info)
            return

        for item in self._payload.data:
            ao_data_response = await get_item_price_from_ao_prices_data(item)
            self._update_item_price(ao_data_response)
        return
