#! /usr/bin/python3

import os
import territory.territory

import datatypes.size
import datatypes.location

class Parser(object):
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def parse(filename) -> territory.territory.Territory:
        data = []
        try:
            with open(filename, "r") as f:
                data = f.read().split("\n")
        except IOError as e:
            raise IOError(f"Error loading territoryFile={filename}") 

        size = datatypes.size.Size(int(data[0].split("x")[0]), int(data[0].split("x")[1]))
        
        parsed_territory = territory.territory.Territory(size, "init")

        for i, row in enumerate(data[1:]):
            if i >= size.height:
                parsed_territory.description = "\n".join(data[i + 1:-1])
                break
            for j, tile in enumerate(row):
                if tile == "#":
                    parsed_territory.wallAt(datatypes.location.Location(i, j))
                elif tile in [str(n) for n in range(10)]:
                    location = datatypes.location.Location(i, j)
                    for n in range(int(tile)):
                        parsed_territory.put_grain(location)
        
        return parsed_territory

