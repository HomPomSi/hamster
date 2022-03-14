#! /usr/bin/python3



class Size(object):
    """
    """
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        if value < 1:
            raise ValueError(f"Width needs to be at least 1, got {value}")
        elif not isinstance(value, int):
            raise TypeError(f"Width needs to be type int, got {type(value)}")
        self._width = value

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int) -> None:
        if value < 1:
            raise ValueError(f"Height needs to be at least 1, got {value}")
        elif not isinstance(value, int):
            raise TypeError(f"Height needs to be type int, got {type(value)}")
        self._height = value 


    def __str__(self):
        return f"{self._width} x {self._height}"



if __name__ == "__main__":
    pass
