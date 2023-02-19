import fastapi
from fastapi import status as http_status
from fastapi.responses import ORJSONResponse

from src.accounting.routes import router as accounting_routing

from devtools.providers.database import AsyncDatabaseProvider

from src.core.database import get_default_database

router = fastapi.APIRouter()
router.include_router(accounting_routing)


@router.get("/health-check")
async def healthcheck(
    default_database: AsyncDatabaseProvider = fastapi.Depends(get_default_database),
):
    response = {
        "status": True,
        "database": await default_database.health_check(),
    }

    return (
        response
        if all(response.values())
        else ORJSONResponse(
            response, status_code=http_status.HTTP_503_SERVICE_UNAVAILABLE
        )
    )
