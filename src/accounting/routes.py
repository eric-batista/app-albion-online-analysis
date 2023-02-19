import fastapi

router = fastapi.APIRouter(prefix="/accounting", tags=["Accounting"])


@router.get("/item")
def get_item_info():
    return


@router.post("/item")
async def create_new_item():
    return


@router.put("/item/{id}")
async def update_item(id: str):
    return id
