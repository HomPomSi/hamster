#! /usr/bin/python3




class TerritoryException(Exception):
    def __init__(self, msg: str = "") -> None:
        self._msg = "Failed interacting with territory."
        super().__init__(f"{self._msg} {msg}")



class NoGrainAvailableException(TerritoryException):
    def __init__(self, msg: str = "") -> None:
        self._msg = f"No grain available."
        super().__init__(f"{self._msg} {msg}")

class GrainPileFullException(TerritoryException):
    def __init__(self, msg: str = "") -> None:
        self._msg = f"GrainPile is already full."
        super().__init__(f"{self._msg} {msg}")

class OutOfTerritoryBoundariesException(TerritoryException):
    def __init__(self, msg: str = "") -> None:
        self._msg = "Out of territory boundaries."
        super().__init__(f"{self._msg} {msg}")

