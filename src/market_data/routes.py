import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.core.database import get_default_database
from src.market_data import domain, models

router = fastapi.APIRouter(prefix="/market-data", tags=["Accounting"])


@router.post("/", response_model=models.CalculateGatheringResponse)
async def get_gathering_profit(
    payload: models.CalculateGatheringRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await domain.CalculateGatheringProfit(
        payload=payload, default_database=default_database
    ).execute()


@router.post("/diaries")
async def get_diary_profit(
    payload: models.CalculateGatheringRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await domain.CalculateDiaryProfit(
        default_database=default_database
    ).execute()
