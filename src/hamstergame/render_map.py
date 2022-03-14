#! /usr/bin/python3

import territory.territory


class RenderMap(object):
    def __init__(self, ter: territory.territory.Territory) -> None:
        self._base_map = self._transform_territory(ter)
        self._states = []
    
    @property
    def base_map(self) -> list:
        return self._base_map

    def _transform_territory(self, ter: territory.territory.Territory) -> list:
        return [[int(tile.is_wall()) for tile in row] for row in ter.grid]

    def get_state(self, index: int) -> list:
        if not isinstance(index, int):
            raise ValueError(f"StateIndex expected to be type int, got {type(index)}")
        elif index < 0 and index >= len(self._states):
            raise IndexError(f"StateIndex out of range, got {index}")
        return self._states[index]

    def add_state(self, state: tuple) -> None:
        """
            state:
            (
                (
                    hamster_location,
                    hamster_direction
                ),
                tile_descriptor
            )

            tile_descriptor:
            0 - 9   --> grain_amount
            -1      --> portal
        """
        result = ((state[0], state[1]), state[2])
        self._states.append(result)

    def __len__(self) -> int:
        return len(self._states)

    def __str__(self) -> str:
        tmp = [f"{i:0{len(str(len(self._states)))}d} :: ({state[0][0].column_index:02d} | {state[0][0].row_index:02d}) --> {state[0][1].name:5s} <{state[1]}>" for i, state in enumerate(self._states)]
        return "\n".join(tmp)
