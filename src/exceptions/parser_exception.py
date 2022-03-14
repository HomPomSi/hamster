#! /usr/bin/python3



class ParserException(Exception):
    def __init__(self, msg):
        self._msg = "Error parsing territory file."
        super().__init__(f"{self._msg} {msg}")



class InvalidSizeFormatException(ParserException):
    def __init__(self, msg: str) -> None:
        self._msg = "Size definition is incorrect."
        super().__init__(f"{self._msg} {msg}")

class InvalidPortalSettingsException(ParserException):
    def __init__(self, msg: str) -> None:
        self._msg = "Territory file contains and insufficent amount of portal notations."
        super().__init__(f"{self._msg} {msg}")
        
