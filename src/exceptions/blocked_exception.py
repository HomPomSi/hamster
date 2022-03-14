#! /usr/bin/python3



class BlockedException(Exception):
    def __init__(self, msg: str) -> None:
        self._msg = "Path is blocked."
        super().__init__(f"{self._msg} {msg}")



class FrontIsBlockedException(BlockedException):
    def __init__(self, msg: str = "") -> None:
        self._msg = f"There is something in the front that blocks our path."
        super().__init__(f"{self._msg} {msg}")

class PortalClosedException(BlockedException):
    def __init__(self, msg: str) -> None:
        self._msg = "There is no portal to travel threw."
        super().__init__(f"{self._msg} {msg}")

