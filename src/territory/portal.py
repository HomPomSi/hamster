#! /usr/bin/ppython3


import datatypes.location



class Portal(object):
    def __init__(self, source: datatypes.location.Location, destination: datatypes.location.Location) -> None:
        self._source = source
        self._destination = destination

    
    @property
    def source(self) -> datatypes.location.Location:
        return self._source

    @property
    def destination(self) -> datatypes.location.Location:
        return self._destination

    def get_endpoints(self) -> tuple:
        return self._source, self._destination
