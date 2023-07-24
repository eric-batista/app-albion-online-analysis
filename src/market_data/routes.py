import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.core.database import get_default_database
from src.market_data import domain, models

router = fastapi.APIRouter(prefix="/market-data", tags=["Accounting"])


@router.post("/")
async def get_market_data(
    payload: models.ItemsListRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await domain.GetItemsInfosFromAOData(
        payload=payload, default_database=default_database
    ).execute()


@router.get("/{item_id}")
async def get_best_place_to_sell_item(
    item_id: str,
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await domain.GetBestPlaceToSellItem(
        item_id=item_id, default_database=default_database
    ).execute()
