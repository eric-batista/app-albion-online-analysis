from uuid import UUID

import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.accounting.models import ItemsListRequest, CalculateGatheringRequest, CalculateGatheringResponse
from src.accounting.use_cases import GetItemsInfosFromAoDataUseCase, ListItemsInfosHistoryUseCase, CalculateGatheringProfitUseCase
from src.core.database import get_default_database

router = fastapi.APIRouter(prefix="/accounting", tags=["Data"])


@router.post("/items")
async def get_item_info_from_ao_data(
    items: ItemsListRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await GetItemsInfosFromAoDataUseCase(
        items=items, default_database=default_database
    ).execute()


@router.get("/items")
async def lists_items_infos_history(
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await ListItemsInfosHistoryUseCase(
        default_database=default_database
    ).execute()


@router.post("/gathering", response_model=CalculateGatheringResponse)
async def get_gathering_profit(
    payload: CalculateGatheringRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await CalculateGatheringProfitUseCase(
        payload=payload,
        default_database=default_database
    ).execute()
