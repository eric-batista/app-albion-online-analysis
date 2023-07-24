from datetime import datetime
from uuid import UUID

from devtools.models import Model


class ExpectedProfitHistoryCreate(Model):
    id: UUID
    created_at: datetime


class ExpectedProfitHistory(Model):
    id: UUID
    created_at: datetime
