import math
import pygame
import utils.config
from utils.spritesheet import SpriteSheet


"""utils: file for loading backgrounds and other objects"""
"""inherits from Spritesheet"""
class Background(SpriteSheet):
    def __init__(self, file_name, screen):
        super().__init__(file_name)
        self.map = []
        self.image = pygame.Rect(0, 0, utils.config.SCREEN_HEIGHT,
                                    utils.config.SCREEN_WIDTH)
        self.screen = screen
    
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
        xpos = 0
        for line in self.map:
            ypos = 0
            #each num in line
            for tileNum in line:
                #for each tile in map, get corresponding tile image
                #convert the string to an int
                tile = self.get_image(int(tileNum))
                #new image size of the screen
                #self.image.blit(tile, line, int(tileNum))
                rect = pygame.Rect(xpos, ypos, utils.config.SCREEN_WIDTH, utils.config.SCREEN_HEIGHT)
                ypos = ypos + 1
                self.test_background(line, tileNum)
            xpos = xpos + 1  

        self.screen.blit(tile, rect)
    
    #testing background methods
    def test_background(self, line, tileNum):
        #tile num is right, then loading the tiles is wrong and the tiles aren't getting loaded to the correct
        #spot on the rect
        print("TileNum: " + tileNum)