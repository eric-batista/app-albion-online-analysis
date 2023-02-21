from datetime import datetime

from devtools.models import Model


class AlbionOnlineDataResponse(Model):
    item_id: str
    city: str
    quality: int
    sell_price_min: int
    sell_price_min_date: datetime
    sell_price_max: int
    sell_price_max_date: datetime
    buy_price_min: int
    buy_price_min_date: datetime
    buy_price_max: int
    buy_price_max_date: datetime
