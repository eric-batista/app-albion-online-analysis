import sqlalchemy as sa
from devtools.providers.database import Entity
from devtools.providers.database.types import GUUID

from src.utils.enums import CitiesEnum


class ItemsEntity(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True)
    city = sa.Column(sa.Enum(CitiesEnum), index=True)
    last_sell_price = sa.Column(sa.Integer(), index=True)
    last_buy_price = sa.Column(sa.Integer(), index=True)
    last_price_date = sa.Column(sa.DateTime(), index=True)
    created_at = sa.Column(sa.DateTime())
    updated_at = sa.Column(sa.DateTime())


class ItemsHistoryEntity(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True)
    city = sa.Column(sa.Enum(CitiesEnum), index=True)
    last_sell_price = sa.Column(sa.Integer(), index=True)
    last_buy_price = sa.Column(sa.Integer(), index=True)
    last_price_date = sa.Column(sa.DateTime(), index=True)
    created_at = sa.Column(sa.DateTime())
    updated_at = sa.Column(sa.DateTime())
