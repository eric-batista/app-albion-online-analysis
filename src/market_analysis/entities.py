import sqlalchemy as sa
from devtools.providers.database import Entity
from devtools.providers.database.types import GUUID


class Items(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    created_at = sa.Column(sa.DateTime())
    updated_at = sa.Column(sa.DateTime())
