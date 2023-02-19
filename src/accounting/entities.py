import sqlalchemy as sa
from devtools.providers.database import Entity
from devtools.providers.database.types import GUUID


class ItemEntity(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True)
