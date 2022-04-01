#! /usr/bin/python3

import territory.territory
import territory.tile
import territory.wall
import territory.grain_pile
import datatypes.location
import datatypes.direction
import hamster.hamster
import hamstergame.render_map

import exceptions.max_steps_exception

import os
import time
import pygame
print("\n")

class Hamstergame(object):
    def __init__(self, territory: territory.territory.Territory) -> None:
        self._territory = territory
        
        self._render_map = hamstergame.render_map.RenderMap(self._territory)

        pygame.init()
        pygame.mixer.init()
        
        self._clock = pygame.time.Clock()
        self._tickrate = 60
    
        self._display = pygame.display.set_mode((self._territory.size.width * 64, self._territory.size.height * 64))

        self._images = self._load_images()
        
        self._render_all()

        self._steps = 0
        self._MAX_STEPS = 9999

    @property
    def territory(self) -> territory.territory.Territory:
        return self._territory
    
    def add_state(self, location: datatypes.location.Location, direction: datatypes.direction.Direction) -> None:
        descriptor = 0
        tile = self._territory.grid[location.row_index][location.column_index]
        if tile.is_portal():
            descriptor = -1
        else:
            descriptor = tile.grain_pile.amount

        self._render_map.add_state((location, direction, descriptor))

        if len(self._render_map) >= self._MAX_STEPS:
            raise exceptions.max_steps_exception.MaxStepsException(f"Hamstergame reached its maximum stepcount")
        self._steps += 1
        

    def run(self) -> None:
        t = time.time()
        state_index = 0
        running = True
        print(self._render_map)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            if running:
                if time.time() - t > 0.2:
                    t = time.time()
                    self._render_state(state_index)
                    state_index += 1
                    if state_index >= len(self._render_map):
                        running = False


            self._clock.tick(self._tickrate)
    
    def _load_images(self) -> dict:
        images = {}
        for entity in os.listdir("../resources/images"):
            if entity.endswith(".png"):
                images[entity[:-4]] = pygame.image.load(f"../resources/images/{entity}")
        return images
    
    def _render_base(self) -> None:
        grid = self._render_map.base_map
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                if tile == 1:
                    self._display.blit(self._images["wall"], (x * 64, y * 64))
                else:
                    self._display.blit(self._images["tile_base"], (x * 64, y * 64))
        pygame.display.update() 
    
    def _render_all(self) -> None:
        self._render_base()
        grid = self._territory.grid
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                if not tile.is_wall():
                    if tile.is_portal():
                        self._display.blit(self._images["portal"], (x * 64, y * 64)) 
                    else:
                        self._display.blit(self._images[f"grain{tile.grain_pile.amount}"], (x * 64, y * 64))
        pygame.display.update()        

    def _render_state(self, index: int) -> None:
        current = self._render_map.get_state(index)
        old = self._render_map.get_state(index - 1)
        if index == 0:
            old = current

        self._display.blit(self._images["tile_base"], (old[0][0].column_index * 64, old[0][0].row_index * 64))
        if old[1] == -1:
            self._display.blit(self._images["portal"], (old[0][0].column_index * 64, old[0][0].row_index * 64))
        else:
            self._display.blit(self._images[f"grain{old[1]}"], (old[0][0].column_index * 64, old[0][0].row_index * 64))
            
        self._display.blit(self._images["tile_base"], (current[0][0].column_index * 64, current[0][0].row_index * 64))
        if current[1] == -1:
            self._display.blit(self._images["portal"], (current[0][0].column_index * 64, current[0][0].row_index * 64))
        else:
            self._display.blit(self._images[f"grain{current[1]}"], (current[0][0].column_index * 64, current[0][0].row_index * 64))
        
        self._display.blit(pygame.transform.rotate(self._images["hamster"], current[0][1].value * 90), (current[0][0].column_index * 64, current[0][0].row_index * 64))
        pygame.display.update([(old[0][0].column_index * 64, old[0][0].row_index * 64, 64, 64), (current[0][0].column_index * 64, current[0][0].row_index * 64, 64, 64)])

        



































