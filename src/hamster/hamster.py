#! /usr/bin/python3

import hamstergame.hamstergame
import datatypes.direction
import datatypes.location

class Hamster(object):
    def __init__(self, game: hamstergame.hamstergame.Hamstergame, location: datatypes.location.Location, grain_count: int = 0) -> None:
        self._game = game
        self._grainCount = grain_count
        self._location = location
        self._direction = datatypes.direction.Direction.EAST

    @property
    def grainCount(self) -> int:
        return self._grainCount

    def _set_location(self, location: datatypes.location.Location) -> None:
        if not self._game.territory.isWall(location):
            self._location = location

    def move(self) -> None:
        if self._direction == datatypes.direction.Direction.NORTH:
            self._set_location(datatypes.location.Location(self._location.row_index, self._location.column_index - 1))
        elif self._direction == datatypes.direction.Direction.EAST:
            self._set_location(datatypes.location.Location(self._location.row_index + 1, self._location.column_index))
        elif self._direction == datatypes.direction.Direction.SOUTH:
            self._set_location(datatypes.location.Location(self._location.row_index, self._location.column_index + 1))
        else:
            self._set_location(datatypes.location.Location(self._location.row_index - 1, self._location.column_index))
    
    def turnRight(self) -> None:
        if self._direction == datatypes.direction.Direction.NORTH:
            self._direction = datatypes.direction.Direction.EAST
        elif self._direction == datatypes.direction.Direction.EAST:
            self._direction = datatypes.direction.Direction.SOUTH
        elif self._direction == datatypes.direction.Direction.SOUTH:
            self._direction = datatypes.direction.Direction.WEST
        else:
            self._direction = datatypes.direction.Direction.NORTH
    
    def pickGrain(self) -> None:
        self._game.territory.pick_grain(self._location)
        self._grainCount += 1
    
    def putGrain(self) -> None:
        if self._grainCount <= 0:
            raise ValueError(f"Hamster is out of grains")
        self._game.territory.put_grain(self._location)
        self._grainCount -= 1

    def grainAvailable(self) -> bool:
        return self._game.territory.grain_available(self._location)
    
    def frontIsClear(self) -> bool:
        try:
            if self._direction == datatypes.direction.Direction.NORTH:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index, self._location.column_index - 1))
            elif self._direction == datatypes.direction.Direction.EAST:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index + 1, self._location.column_index))
            elif self._direction == datatypes.direction.Direction.SOUTH:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index, self._location.column_index + 1))
            else:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index - 1, self._location.column_index))
        except ValueError as e:
            return False
    

