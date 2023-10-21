import math
import pygame
import utils.config
from utils.spritesheet import SpriteSheet


"""utils: file for loading backgrounds and other objects"""
"""inherits from Spritesheet"""
class Background(SpriteSheet):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.map = []
        self.image = pygame.Rect(0, 0, utils.config.SCREEN_HEIGHT,
                                    utils.config.SCREEN_WIDTH)
    
    #load maps from /maps 
    #reads from .txt file and converts to a list
    def load_map(self, map_file):
            #open file
            with open('utils/maps/' + map_file + ".txt") as mfile:
                #string in textIOwrapper
                for line in mfile:
                    tiles =[]
                    #int for length of line, increment 2
                    for i in range(0, len(line) -1, 2):
                        #add int to tiles list
                        tiles.append(line[i])
                    #append the tile rows to the map list
                    self.map.append(tiles)
                
                print(self.map)
                #now render the list
                self.render_map()

    #render the map
    def render_map(self):
        
        #for each row in map
        for line in self.map:
            #each num in line
            for tileNum in line:
                #for each tile in map, get corresponding tile image
                #convert the string to an int
                tile = self.get_image(int(tileNum))
                #new image size of the screen
                self.image.blit(tile, line, int(tileNum))
                
    