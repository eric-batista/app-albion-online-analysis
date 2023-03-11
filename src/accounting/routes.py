import fastapi

from src.accounting.routing.gathering_routes import router as gathering_routing
from src.accounting.routing.items_routes import router as items_routing

router = fastapi.APIRouter(prefix="/accounting", tags=["Accounting"])

router.include_router(items_routing)
router.include_router(gathering_routing)
