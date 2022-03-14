#! /usr/bin/python3

import hamstergame.hamstergame
import datatypes.direction
import datatypes.location

import exceptions.blocked_exception
import exceptions.territory_exception

class Hamster(object):
    def __init__(self, game: hamstergame.hamstergame.Hamstergame, location: datatypes.location.Location, grain_count: int = 0) -> None:
        self._game = game
        self._grainCount = grain_count
        self._location = location
        self._direction = datatypes.direction.Direction.EAST
        self._game.add_state(self._location, self._direction)
    
    def _get_location(self) -> datatypes.location.Location:
        return self._location

    def _set_location(self, location: datatypes.location.Location) -> None:
        if not self._game.territory.isWall(location):
            self._location = location
        else:
            raise exceptions.blocked_exception.FrontIsBlockedException("Front is blocked by a wall")
    
    def teleport(self) -> None:
        if not self._game.territory.isPortal(self._location):
            raise exceptions.blocked_exception.PortalClosedException(f"No portal at {self._location}")
        
        source, destination = self._game.territory.getPortal(self._location).get_endpoints()
        if source == self._location:
            self._location = destination
            print(f"[DEBUG] - use portal to move hamster from {source} to {destination}")
        else:
            self._location = source
            print(f"[DEBUG] - use portal to move hamster from {destination} to {source}")
            
        self._game.add_state(self._location, self._direction)

    def move(self) -> None:
        print(f"[DEBUG] - move hamster in {self._direction} direction")
        if self._direction == datatypes.direction.Direction.NORTH:
            self._set_location(datatypes.location.Location(self._location.row_index - 1, self._location.column_index))
        elif self._direction == datatypes.direction.Direction.EAST:
            self._set_location(datatypes.location.Location(self._location.row_index, self._location.column_index + 1))
        elif self._direction == datatypes.direction.Direction.SOUTH:
            self._set_location(datatypes.location.Location(self._location.row_index + 1, self._location.column_index))
        else:
            self._set_location(datatypes.location.Location(self._location.row_index, self._location.column_index - 1))
        self._game.add_state(self._location, self._direction)


    def turnRight(self) -> None:
        debug = f"[DEBUG] - turn hamster to the right from {self._direction}"
        if self._direction == datatypes.direction.Direction.NORTH:
            self._direction = datatypes.direction.Direction.EAST
        elif self._direction == datatypes.direction.Direction.EAST:
            self._direction = datatypes.direction.Direction.SOUTH
        elif self._direction == datatypes.direction.Direction.SOUTH:
            self._direction = datatypes.direction.Direction.WEST
        else:
            self._direction = datatypes.direction.Direction.NORTH
        print(f"{debug} to {self._direction}")
        self._game.add_state(self._location, self._direction)
    
    def pickGrain(self) -> None:
        try:
            self._game.territory.pick_grain(self._location)
        except exceptions.territory_exception.NoGrainAvailableException as e:
            raise exceptions.territory_exception.NoGrainAvailableException(f"Theres no grains on tile {self._location}")
        print(f"[DEBUG] - picking grain at {self._location}")
        self._grainCount += 1
        self._game.add_state(self._location, self._direction)
    
    def putGrain(self) -> None:
        if self._grainCount <= 0:
            raise exceptions.territory_exception.NoGrainAvailableException("Hamster is out of grains")
        try:
            self._game.territory.put_grain(self._location)
        except exceptions.territory_exceptions.GrainPileFullException as e:
            raise exceptions.territory_exceptions.GrainPileFullException(f"GrainPile at {self._lcoation} is already full")
        print(f"[DEBUG] - put grain at {self._location}")
        self._grainCount -= 1
        self._game.add_state(self._location, self._direction)
    
    def hasGrain(self) -> bool:
        return self._grainCount > 0

    def grainAvailable(self) -> bool:
        return self._game.territory.grain_available(self._location)
    
    def grainPileIsFull(self) -> bool:
        return self._game.territory.grain_pile_is_full(self._location)

    def portalIsOpen(self) -> bool:
        return self._game.territory.isPortal(self._location)

    def frontIsClear(self) -> bool:
        try:
            if self._direction == datatypes.direction.Direction.NORTH:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index - 1, self._location.column_index))
            elif self._direction == datatypes.direction.Direction.EAST:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index, self._location.column_index + 1))
            elif self._direction == datatypes.direction.Direction.SOUTH:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index + 1, self._location.column_index))
            else:
                return not self._game.territory.isWall(datatypes.location.Location(self._location.row_index, self._location.column_index - 1))
        except ValueError as e:
            return False
    
    def write(self, msg: str) -> None:
        print(f"[HAMSTER] - {msg}")

