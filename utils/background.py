import math
import pygame
import utils.config
from spritesheet import SpriteSheet


"""utils: file for loading backgrounds and other objects"""
"""inherits from Spritesheet"""
"""to do:
1. draw tiles on map
2. figure out camera situation
3. make sure it works lol 
4. fix render map? Not sure how its drawing to screen? """
class Background(SpriteSheet):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.map = []
    
    #load maps from /maps 
    #reads from .txt file and converts to a list
    def load_map(self, file_name):
            with open('maps/' + file_name + ".txt") as map_file:
                for line in map_file:
                    tiles =[]
                    for i in range(0, len(line) -1, 2):
                        tiles.append(line[i])
                    self.map.append(tiles)
                print(self.map)

    #using list, get tiles from spritesheet
    def render_map(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                #for each tile in map, get corresponding tile image
                image = self.get_image(tile)
                rect = pygame.Rect(x_pos * utils.config.SCALE, y_pos * utils.config.SCALE,
                                utils.config.SCALE, utils.config.SCALE)
    