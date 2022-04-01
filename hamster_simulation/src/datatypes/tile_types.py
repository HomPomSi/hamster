#! /usr/bin/python3

import enum


class TileTypes(enum.Enum):
    BASE, WALL, GRAIN_PILE, PORTAL = range(4)


