import fastapi
from devtools.providers.database import AsyncDatabaseProvider

from src.core.database import get_default_database
from src.player_stats import domain, models

router = fastapi.APIRouter(prefix="/player-stats", tags=["Players Stats"])


@router.post("/")
async def create_new_player_stats(
    payload: models.PlayerStatsPayload = fastapi.Body(),
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    return await domain.CreatePlayerStats(
        payload=payload, default_database=default_database
    ).execute()
