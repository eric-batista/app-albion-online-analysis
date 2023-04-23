from decimal import Decimal
from uuid import UUID

from devtools.models import Model

from src.utils.enums import ItemTier


class PlayerStatsModel(Model):
    id: UUID


class PlayerStatsCreate(Model):
    id: UUID
    name: str


class PlayerStatsPayload(Model):
    name: str


class CombatStatsModel(Model):
    id: UUID
    name: str


class CombatStatsCreate(Model):
    id: UUID
    name: str


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
