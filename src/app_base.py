#! /usr/bin/python3

import hamster.hamster
import hamstergame.hamstergame

import datatypes.location
import territory.territory
import territory.parser

import exceptions.max_steps_exception

TEST = False
#TEST = True 
if TEST:
    import test.verify_territories
    quit()


class AppBase(object):
    def __init__(self, ter: str = "") -> None:
        if ter == "":
            raise ArgumentError("Missing territory path")
        self._territory = territory.parser.Parser().parse(ter)
        print(self._territory)
        self._game = hamstergame.hamstergame.Hamstergame(self._territory)
        self._game._MAX_STEPS = 999999
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
