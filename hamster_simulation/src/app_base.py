#! /usr/bin/python3

import hamster.hamster
import hamstergame.hamstergame

import datatypes.location
import territory.territory
import territory.parser

import exceptions.max_steps_exception

import typing




class AppBase(object):
    """
    Parent class for managing the hamster simulation.
    Forces the user to implement an _execute_hamstergame method and runs/renders
    the simulation when object is created.
    To avoid in getting stuck in calculating the simulation and not getting to render 
    it, the _execute_hamstergame method is terminated after MAX_STEPS has been reached.
    The simulation data is saved at the end.
    """
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
        print("[DEBUG] - starting render process")
        try:
            self._game.run()
        except:
            print("[DEBUG] - render process has been interrupted")
        finally:
            self._game.save_data()

    def _execute_hamstergame(self) -> None:    
        raise NotImplementedError("implement meeeeee")


if __name__ == "__main__":
    AppBase()
