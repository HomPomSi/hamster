#! /usr/bin/python3

import hamster.hamster
import hamstergame.hamstergame

import datatypes.location
import territory.territory
import territory.parser

import exceptions.max_steps_exception

import typing



class AppBase(object):
    def __init__(self, ter: typing.Union[str, territory.territory.Territory]) -> None:
        if isinstance(ter, str):
            self._territory = territory.parser.Parser().parse(ter)
        elif isinstance(ter, territory.territory.Territory):
            self._territory = ter

        self._game = hamstergame.hamstergame.Hamstergame(self._territory)
        self._game._MAX_STEPS = 1048576
        self._paule = hamster.hamster.Hamster(self._game, datatypes.location.Location(1, 1))
        try:
            self._execute_hamstergame()
        except exceptions.max_steps_exception.MaxStepsException as e:
            print("[WARNING] - reached MAX_STEPS, starting render process")
        except Exception as e:
            print(f"[WARNING] - other exception occured during execution, starting render process\n[ERROR] - {e}\n")
        self._game.run()

    def _execute_hamstergame(self) -> None:    
        raise NotImplementedError("implement meeeeee")


if __name__ == "__main__":
    AppBase()
