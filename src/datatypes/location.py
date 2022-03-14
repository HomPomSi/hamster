#! /usr/bin/python3



class Location(object):
    """
    """
    def __init__(self, row: int, column: int) -> None:
        self._row_index = row
        self._column_index = column


    @property
    def row_index(self) -> int:
        return self._row_index

    @row_index.setter
    def row_index(self, value: int) -> None:
        if value < 0:
            raise ValueError(f"Row index needs to be at least 0, got {value}")
        elif not isinstance(value, int):
            raise TypeError(f"Row index needs to be type int, got {type(value)}")
        self._row_index = value

    @property
    def column_index(self) -> int:
        return self._column_index

    @column_index.setter
    def column_index(self, value: int) -> None:
        if value < 0:
            raise ValueError(f"Column index needs to be at least 0, got {value}")
        elif not isinstance(value, int):
            raise TypeError(f"Column index needs to be type int, got {type(value)}")
        self._column_index = value
    
    def __eq__(self, other) -> bool:
        return self._row_index == other.row_index and self._column_index == other.column_index

    def __str__(self) -> str:
        return f"{self._row_index}|{self._column_index}"



if __name__ == "__main__":
    pass
