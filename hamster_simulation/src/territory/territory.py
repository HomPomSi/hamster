#! /usr/bin/python3

import datatypes.size
import datatypes.location
import datatypes.direction
import datatypes.tile_types

import territory.grain_pile
import territory.wall
import territory.tile
import territory.portal

import exceptions.territory_exception

class Territory(object):   
    def __init__(self, size: datatypes.size.Size, description: str = "") -> None:
        self._size = size
        self._grid = []
        self._description = description
        for row in range(self._size.height):
            self._grid.append([])
            for column in range(self._size.width):
                tile = territory.tile.Tile(datatypes.location.Location(row, column))
                self._grid[-1].append(tile)

    @property
    def size(self) -> datatypes.size.Size:
        return self._size

    @size.setter
    def size(self, value: datatypes.size.Size) -> None:
        print("[WARNING] Territorys size is final")
    
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Territory description needs to be type str, got {type(value)}")
        self._description = value
    
    @property
    def grid(self) -> list:
        return self._grid
    
    @grid.setter
    def grid(self, value: list) -> None:
        print("[WARNING] Territorys grid is final")
    
    def __len__(self) -> datatypes.size.Size:
        return self._size

    def __str__(self):
        description = f"---\n{self._size}"
        for row in self._grid:
            description = f"{description}\n"
            for tile in row:
                if tile.is_wall():
                    description = f"{description}#"
                elif tile.is_portal():
                    description = f"{description}O"
                else:
                    description = f"{description}{str(tile.grain_pile.amount)}"
        description = f"{description}\n...\n{self._description}".replace("0", " ")
        return description
    
    def isWall(self, location: datatypes.location.Location) -> bool:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to get wall info")
        return self._grid[location.row_index][location.column_index].is_wall()

    def wallAt(self, location: datatypes.location.Location) -> None:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to set wall")
        self._grid[location.row_index][location.column_index].set_wall()
    
    def isPortal(self, location: datatypes.location.Location) -> bool:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to get portal info")
        return self._grid[location.row_index][location.column_index].is_portal()

    def setPortal(self, source: datatypes.location.Location, destination: datatypes.location.Location) -> None:
        if source.row_index > self._size.height - 1 or source.column_index > self._size.width - 1:  
            if destination.row_index > self._size.height - 1 or destination.column_index > self._size.width - 1:  
                raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to set portal")
            elif self._grid[destination.row_index][destination.column_index].is_portal() or self._grid[source.row_index][source.column_index].is_portal():
                raise exceptions.territory_exception.PortalInterceptionException(f"{source} or {destination} already contains portal")
        portal = territory.portal.Portal(source, destination)
        self._grid[source.row_index][source.column_index].portal = portal
        self._grid[destination.row_index][destination.column_index].portal = portal
    
    def getPortal(self, location: datatypes.location.Location) -> territory.portal.Portal:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to get portal")
        if not self._grid[location.row_index][location.column_index].is_portal():
            raise exeptions.blocked_exception.PortalClosedException(f"No portal at {location}")
        return self._grid[location.row_index][location.column_index].portal
    
    def put_grain(self, location: datatypes.location.Location) -> None:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to put grain")
        self._grid[location.row_index][location.column_index].put_grain()

    def pick_grain(self, location: datatypes.location.Location) -> None:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1: 
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to pick grain")
        self._grid[location.row_index][location.column_index].pick_grain()

    def grain_available(self, location: datatypes.location.Location) -> bool:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to get grain info")
        return self._grid[location.row_index][location.column_index].grain_available()

    def grain_pile_is_full(self, location: datatypes.location.Location) -> bool:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:
            raise exceptions.territory_exceptin.OutOfTerritoryBoundariesExcception(f"Trying to get grain info")
        return self._grid[location.row_index][location.column_index].grain_pile_is_full()
        
