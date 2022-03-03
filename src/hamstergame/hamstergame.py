#! /usr/bin/python3

import territory.territory


class Hamstergame(object):
    def __init__(self, territory: territory.territory.Territory) -> None:
        self._territory = territory

    @property
    def territory(self) -> territory.territory.Territory:
        return self._territory

        
