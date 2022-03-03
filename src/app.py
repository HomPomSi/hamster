#! /usr/bin/python3

import hamster.hamster
import hamstergame.hamstergame

from datatypes import location
from territory import parser

class App(object):
    def __init__(self) -> None:
        self._territory = parser.Parser.parse("../resources/territories/blank-8x8.ter")
        self._territory = parser.Parser.parse("../resources/territories/max-grain-8x8.ter")
        self._game = hamstergame.hamstergame.Hamstergame(self._territory)
        self._paule = hamster.hamster.Hamster(self._game, location.Location(1, 1))
    
    def main(self) -> None:    
        self._paule.pickGrain()

    def run(self) -> None:
        self._game.run()

if __name__ == "__main__":
    app = App()
    app.run()
