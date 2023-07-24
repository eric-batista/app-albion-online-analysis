from decimal import Decimal
from uuid import UUID

from devtools.models import Model

from src.utils.enums import ItemTier


class BaseRequestModel(Model):
    name: str
    level: int
    max_tier_enable: ItemTier


class BaseCreateModel(BaseRequestModel):
    id: UUID


class CombatStatsModel(Model):
    id: UUID
    name: str


class CombatStatsCreate(BaseCreateModel):
    id: UUID
    name: str


class CombatStatsRequest(BaseRequestModel):
    pass


class CraftingSpecialistModel(Model):
    id: UUID
    name: str
    bonus_item_focus: Decimal
    bonus_class_focus: Decimal
    bonus_item_quality: Decimal
    bonus_class_quality: Decimal
    level: int


class CraftingStatsModel(Model):
    id: UUID
    name: str
    bonus_item_focus: Decimal
    bonus_class_focus: Decimal
    level: int
    max_tier_enable: ItemTier
    crafting_specialist_id: UUID
    crafting_specialist: CraftingSpecialistModel


class CraftingStatsCreate(BaseCreateModel):
    pass


class PlayerStatsModel(Model):
    id: UUID


class PlayerStatsCreate(Model):
    id: UUID
    name: str


class PlayerStatsPayload(Model):
    name: str
    combat_stats: CombatStatsCreate
    crafting_stats: CraftingStatsCreate
