from datetime import datetime
from typing import List, Dict
from uuid import UUID

from devtools.models import Model

from src.utils.enums import CitiesEnum, ItemsEnum


class ItemModel(Model):
    id: UUID
    name: str
    city: CitiesEnum
    last_sell_price: int
    last_buy_price: int
    last_price_date: datetime
    created_at: datetime
    updated_at: datetime | None


class ItemCreateRequest(Model):
    name: str
    city: CitiesEnum
    last_sell_price: int
    last_buy_price: int
    last_price_date: datetime


class ItemUpdateRequest(Model):
    pass


class ItemsListRequest(Model):
    items: List[ItemsEnum]


class ItemCreate(Model):
    id: UUID
    name: str
    city: CitiesEnum
    last_sell_price: int
    last_buy_price: int
    last_price_date: datetime
    created_at: datetime
    updated_at: datetime | None = None


class GatheringItems(Model):
    name: str
    quantity: int
    city: CitiesEnum


class CalculateGatheringRequest(Model):
    data: List[GatheringItems]


class GatheringItemsProfit(GatheringItems):
    profit: int


class CalculateGatheringResponse(Model):
    data: List[GatheringItemsProfit]
