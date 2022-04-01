#! /usr/bin/python3



import os

import territory.territory
import territory.portal
import datatypes.size
import datatypes.location

import exceptions.parser_exception



class Parser(object):
    
    @staticmethod
    def parse(filename) -> territory.territory.Territory:
        data = []
        portal_info = []
        try:
            with open(filename, "r") as f:
                data = f.read().split("\n")
            print(f"[DEBUG] - loading territorry_data from {os.getcwd()}/{filename}")
        except IOError as e:
            raise IOError(f"Error loading territoryFile={filename}") 
    
        try:
            size = datatypes.size.Size(int(data[0].split("x")[0]), int(data[0].split("x")[1]))
        except ValueError as e:
            raise exceptions.parser_exception.InvalidSizeFormatException("")

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
                elif tile == "O":
                    portal_info.append(datatypes.location.Location(i, j))
        if not len(portal_info) in [0, 2]:
            raise exceptions.parser_exception.InvalidPortalSettingsException(f"Read in {len(portal_info)} portals.")
        if len(portal_info) == 2:
            parsed_territory.setPortal(portal_info[0], portal_info[1])
        
        return parsed_territory


if __name__ == "__main__":
    pass
