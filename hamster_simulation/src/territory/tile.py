#! /usr/bin/python3

import datatypes.location
import datatypes.tile_types
import territory.grain_pile
import territory.portal

import exceptions.territory_exception



class Tile(object):
    def __init__(self, location: datatypes.location.Location, tile_type: datatypes.tile_types.TileTypes = datatypes.tile_types.TileTypes.BASE, grain_amount: int = 0) -> None:
        self._location = location
        self._grain_pile = territory.grain_pile.GrainPile(self._location, grain_amount)
        self._portal = None
        self._type = tile_type

    def is_wall(self) -> bool:
        return self._type == datatypes.tile_types.TileTypes.WALL

    def is_portal(self) -> bool:
        return self._type == datatypes.tile_types.TileTypes.PORTAL
    
    @property
    def portal(self) -> territory.portal.Portal:
        return self._portal
    
    @portal.setter
    def portal(self, portal: territory.portal.Portal) -> None:
        self._portal = portal
        self._type = datatypes.tile_types.TileTypes.PORTAL

    @property
    def grain_pile(self) -> territory.grain_pile.GrainPile:
        return self._grain_pile
    
    def grain_available(self) -> bool:
        return self._grain_pile.amount > 0
        
    def grain_pile_is_full(self) -> bool:
        return self._grain_pile.amount >= 9

    def set_wall(self) -> None:
        self._type = datatypes.tile_types.TileTypes.WALL
    
    def put_grain(self) -> None:
        if not self._type in [datatypes.tile_types.TileTypes.WALL, datatypes.tile_types.TileTypes.PORTAL]:
            if self._grain_pile.amount >= 9:
                raise exceptions.territory_exception.GrainPileFullException("GrainPile on tile already full.")
            self._grain_pile = territory.grain_pile.GrainPile(self._location, self._grain_pile.amount + 1)

    def pick_grain(self) -> None:
        if not self._type in [datatypes.tile_types.TileTypes.WALL, datatypes.tile_types.TileTypes.PORTAL]:
            if self._grain_pile.amount <= 0:
                raise exceptions.territory_exception.NoGrainAvailableException("No grain on tile available")
            self._grain_pile = territory.grain_pile.GrainPile(self._location, self._grain_pile.amount - 1)

    def get_grain(self) -> int:
        return self._grain_pile.amount
