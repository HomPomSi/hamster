#! /usr/bin/python3

import datatypes.size
import datatypes.location
import datatypes.direction
import territory.grain_pile
import territory.wall
import territory.tile

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
                if tile.is_wall:
                    description = f"{description}#"
                else:
                    description = f"{description}{str(tile.grain_pile.amount)}"
        description = f"{description}\n...\n{self._description}".replace("0", " ")
        return description
    
    def isWall(self, location: datatypes.location.Location) -> bool:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise ValueError(f"Trying to get wall info outside the territory boundaries")
        return self._grid[location.row_index][location.column_index].is_wall()

    def wallAt(self, location: datatypes.location.Location) -> None:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise ValueError(f"Trying to set wall outside the territory boundaries")
        self._grid[location.row_index][location.column_index].set_wall()

    def put_grain(self, location: datatypes.location.Location) -> None:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:  
            raise ValueError(f"Trying to put grain outside the territory boundaries")
        self._grid[location.row_index][location.column_index].put_grain()

    def pick_grain(self, location: datatypes.location.Location) -> None:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1: 
            raise ValueError(f"Trying to pick grain outside the territory boundaries")
        self._grid[location.row_index][location.column_index].pick_grain()

    def grain_available(self, location: datatypes.location.Location) -> bool:
        if location.row_index > self._size.height - 1 or location.column_index > self._size.width - 1:
            raise ValueError(f"Trying to get info outside the territory boundaries")
        return self._grid[location.row_index][location.column_index].grain_available()


