#! /usr/bin/python3

import datatypes.location


class GrainPile(object):
    def __init__(self, location: datatypes.location.Location, amount: int) -> None:
        self._location = location
        self._amount = amount

    @property
    def location(self) -> datatypes.location.Location:
        return self._location

    @location.setter
    def location(self, value: datatypes.location.Location) -> None:
        print("[WARNING] GrainPile location is final")

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value: int) -> None:
        if value < 0  and value > 9:
            raise ValueError(f"amount of grains needs to be at least 0 and less than 10, got {value}")
        elif not isinstance(value, int):
            raise TypeError(f"amount of grains type needs to be int, got {type(value)}")
        self._amount = value

    def __str__(self) -> str:
        return f"{self._amount} grains at {str(self._location)}"
