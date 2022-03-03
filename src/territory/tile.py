#! /usr/bin/python3

import datatypes.location
import territory.grain_pile

class Tile(object):
    def __init__(self, location: datatypes.location.Location, grain_amount: int = 0, is_wall: bool = False) -> None:
        self._location = location
        self._grain_pile = territory.grain_pile.GrainPile(self._location, grain_amount)
        self._is_wall = is_wall
    
    @property
    def is_wall(self) -> bool:
        return self._is_wall
    
    @property
    def grain_pile(self) -> territory.grain_pile.GrainPile:
        return self._grain_pile
    
    def grain_available(self) -> bool:
        return self._grain_pile.amount > 0

    def set_wall(self) -> None:
        self._is_wall = True

    def put_grain(self) -> None:
        if not self._is_wall:
            self._grain_pile.amount = self._grain_pile.amount + 1

    def pick_grain(self) -> None:
        if not self._is_wall:
            self._grain_pile.amount = self._grain_pile.amount - 1

    def get_grain(self) -> int:
        return self._grain_pile.amount
