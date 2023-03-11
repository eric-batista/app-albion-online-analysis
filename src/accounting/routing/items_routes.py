import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.accounting.models import ItemsListRequest
from src.accounting.use_cases import (GetItemsInfosFromAoDataUseCase,
                                      ListItemsInfosHistoryUseCase,
                                      UpdateAllItemsPricesUseCase)
from src.core.database import get_default_database

router = fastapi.APIRouter(prefix="/items")


@router.post("/")
async def get_item_info_from_ao_data(
    items: ItemsListRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await GetItemsInfosFromAoDataUseCase(
        items=items, default_database=default_database
    ).execute()


@router.get("/")
async def lists_items_infos_history(
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await ListItemsInfosHistoryUseCase(
        default_database=default_database
    ).execute()


@router.put("/")
async def update_all_items_price(
    payload: None = None,
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await UpdateAllItemsPricesUseCase(
        payload=payload, default_database=default_database
    ).execute()
