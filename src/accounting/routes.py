from uuid import UUID

import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.accounting.models import ItemCreateRequest, ItemUpdateRequest
from src.accounting.use_cases import GetItemInfosUseCase, CreateNewItemUseCase, UpdateItemUseCase
from src.core.database import get_default_database

router = fastapi.APIRouter(prefix="/accounting", tags=["Accounting"])


@router.get("/item/{id}")
async def get_item_info(
    id: UUID,
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await GetItemInfosUseCase(id=id, default_database=default_database).excute()


@router.post("/item")
async def create_new_item(
    payload: ItemCreateRequest,
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await CreateNewItemUseCase(payload=payload, default_database=default_database).execute()


@router.put("/item/{id}")
async def update_item(
    id: UUID,
    payload: ItemUpdateRequest,
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await UpdateItemUseCase(id=id, payload=payload, default_database=default_database).execute()
