import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.accounting import models, use_cases
from src.core.database import get_default_database

router = fastapi.APIRouter(prefix="/gathering")


@router.post("/", response_model=models.CalculateGatheringResponse)
async def get_gathering_profit(
    payload: models.CalculateGatheringRequest = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await use_cases.CalculateGatheringProfitUseCase(
        payload=payload, default_database=default_database
    ).execute()


@router.post("/diaries")
async def get_diary_profit():
    return await use_cases.CalculateDiaryProfitUseCase().execute()
