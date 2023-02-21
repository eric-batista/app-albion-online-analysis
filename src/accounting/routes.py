from uuid import UUID

import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.accounting.models import (ItemCreateRequest, ItemsListRequest,
                                   ItemUpdateRequest)
from src.accounting.use_cases import GetItemsInfosUseCase
from src.core.database import get_default_database

router = fastapi.APIRouter(prefix="/accounting", tags=["Accounting"])


@router.post("/items")
async def get_item_info(
    items: ItemsListRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await GetItemsInfosUseCase(
        items=items, default_database=default_database
    ).execute()
