from decimal import Decimal

import sqlalchemy as sa
from devtools.providers.database import Entity
from devtools.providers.database.types import GUUID
from sqlalchemy.orm import relationship

from src.utils.enums import ItemTier


## Specialist
class CombatSpecialist(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    bonus_item = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_class = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    level = sa.Column(sa.Integer(), default=0)
    combat_id = sa.Column(GUUID(), sa.ForeignKey("combat_stats.id"))
    combat_stats = relationship("CombatStats")


class CraftingSpecialist(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_item_quality = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_class_quality = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    level = sa.Column(sa.Integer(), default=0)
    crafting_id = sa.Column(GUUID(), sa.ForeignKey("crafting_stats.id"))
    crafting_stats = relationship("CraftingStats")


class AlchemystSpecialist(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    level = sa.Column(sa.Integer(), default=0)
    alchemy_id = sa.Column(GUUID(), sa.ForeignKey("alchemy_stats.id"))
    alchemy_stats = relationship("AlchemyStats")


class SousChefSpecialist(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    level = sa.Column(sa.Integer(), default=0)
    sous_chef_id = sa.Column(GUUID(), sa.ForeignKey("sous_chef_stats.id"))
    sous_chef_stats = relationship("SousChefStats")


class HarvesterSpecialist(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    level = sa.Column(sa.Integer())
    harvester_id = sa.Column(GUUID(), sa.ForeignKey("harvester_stats.id"))
    harvester_stats = relationship("HarvesterStats")


class HerbalistSpecialist(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    level = sa.Column(sa.Integer())
    herbalist_id = sa.Column(GUUID(), sa.ForeignKey("herbalist_stats.id"))
    herbalist_stats = relationship("HerbalistStats")


class AnimalCreationSpecialist(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    level = sa.Column(sa.Integer())
    animal_creation_id = sa.Column(GUUID(), sa.ForeignKey("animal_creation_stats.id"))
    animal_creation_stats = relationship("AnimalCreationStats")


## Stats
class CombatStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    max_tier_enable = sa.Column(sa.Enum(ItemTier), nullable=False)
    bonus_class = sa.Column(sa.DECIMAL, nullable=False, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship("PlayerStats", back_populates="combat_stats")


class CraftingStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    max_tier_enable = sa.Column(sa.Enum(ItemTier), nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship("PlayerStats", back_populates="crafting_stats")


class AlchemyStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    max_tier_enable = sa.Column(sa.Enum(ItemTier), nullable=False)
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship("PlayerStats", back_populates="alchemy_stats")


class SousChefStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    max_tier_enable = sa.Column(sa.Enum(ItemTier), nullable=False)
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship("PlayerStats", back_populates="sous_chef_stats")


class RefiningStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    bonus_item_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship("PlayerStats", back_populates="refining_stats")


class HerbalistStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    max_tier_enable = sa.Column(sa.Enum(ItemTier), nullable=False)
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship("PlayerStats", back_populates="herbalist_stats")


class HarvesterStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    max_tier_enable = sa.Column(sa.Enum(ItemTier), nullable=False)
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship("PlayerStats", back_populates="harvester_stats")


class AnimalCreationStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)
    level = sa.Column(sa.Integer(), nullable=False)
    max_tier_enable = sa.Column(sa.Enum(ItemTier), nullable=False)
    bonus_class_focus = sa.Column(sa.DECIMAL, default=Decimal(0.0))
    player_stats_id = sa.Column(GUUID(), sa.ForeignKey("player_stats.id"))
    player_stats_stats = relationship(
        "PlayerStats", back_populates="animal_creation_stats"
    )


class PlayerStats(Entity):
    id = sa.Column(GUUID(), primary_key=True, index=True, nullable=False)
    name = sa.Column(sa.Text(), index=True, nullable=False)

    combat_stats = relationship("CombatStats", lazy="selectin")
    harvester_stats = relationship("HarvesterStats", lazy="selectin")
    animal_creation_stats = relationship("AnimalCreationStats", lazy="selectin")
    herbalist_stats = relationship("HerbalistStats", lazy="selectin")
    sous_chef_stats = relationship("SousChefStats", lazy="selectin")
    alchemy_stats = relationship("AlchemyStats", lazy="selectin")
    crafting_stats = relationship("CraftingStats", lazy="selectin")
    refining_stats = relationship("RefiningStats", lazy="selectin")
