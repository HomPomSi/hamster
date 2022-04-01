#! /usr/bin/python3

import datatypes.location

class Wall(object):
    def __init__(self, location: datatypes.location.Location) -> None:
        self._location = location

    @property
    def location(self) -> datatypes.location.Location:
        return self._location

    @location.setter
    def location(self, value: datatypes.location.Location) -> None:
        print("[WARNING] wall location is final")

