from devtools.providers.database import Entity
from devtools.providers.database.types import UUIDIdMixin
import sqlalchemy as sa

class Item(Entity, UUIDIdMixin):
    name = sa.Colum()
