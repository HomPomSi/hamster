#! /usr/bin/python3



class MaxStepsException(Exception):
    def __init__(self, msg: str) -> None:
        self._msg = "Reached MAX_STEPS"
        super().__init__(f"{self._msg} {msg}")
