#! /usr/bin/python3



# Enumeration parent class
from enum import Enum



class Direction(Enum):
    """
    Enum representing direction of an entity
    EAST  -> 0
    NORTH -> 1
    WEST  -> 2
    SOUTH -> 3
    """
    EAST, NORTH, WEST, SOUTH = range(4)

if __name__ == "__main__":
    print("Direction.DIRECTION -> VALUE")
    for direction in Direction:
        print(f"{direction:19s} ->   {direction.value}")

