import math
import pygame
import utils.config
from utils.spritesheet import SpriteSheet


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
        self.image = pygame.Rect(0, 0, utils.config.SCREEN_HEIGHT,
                                    utils.config.SCREEN_WIDTH)
    
    #load maps from /maps 
    #reads from .txt file and converts to a list
    def load_map(self, map_file):
            with open('utils/maps/' + map_file + ".txt") as mfile:
                for line in mfile:
                    tiles =[]
                    for i in range(0, len(line) -1, 2):
                        tiles.append(line[i])
                    self.map.append(tiles)
                print(self.map)
                #now render the list
                self.render_map()

    #render the map
    def render_map(self):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tileNum in line:
                #for each tile in map, get corresponding tile image
                tile = self.get_image(tileNum)
                #new image size of the screen
                self.image.blit(tile, line, tileNum)
                
    