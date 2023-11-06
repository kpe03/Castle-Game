import math
import pygame
import utils.config
from utils.spritesheet import SpriteSheet


# =================
#  background 
# =================
class Background(SpriteSheet):
    def __init__(self, file_name, screen):
        super().__init__(file_name)
        self.map = []
        self.screen = screen
    
    #load maps from /maps 
    #reads from .txt file and converts to a list
    def load_map(self, map_file):
            #open file
            with open('utils/maps/' + map_file + ".txt") as mfile:
                for line in mfile:
                     number_strings = line.split() #split when whitespace
                     numbers = [int(n) for n in number_strings] #convert to integers
                     self.map.append(numbers) #add the row to the list

                print(self.map)

    #render the map
    #added screen parameter..? maybe that was the problem
    def render_map(self, screen):

        #for each row in map
        ypos = 0
        for line in self.map:
            xpos = 0
            #each num in line
            for tileNum in line:
                #for each tile in map, get corresponding tile image
                #tileNum is a string-- convert to an int
                tile = self.get_image(int(tileNum))
                #new image size of the screen
                rect = pygame.Rect(xpos * utils.config.SCALE, ypos  * utils.config.SCALE, utils.config.SCALE, utils.config.SCALE)
                #blit!
                screen.blit(tile, rect)
                xpos = xpos + 1
                
            ypos = ypos + 1  

    #testing background methods
    def test_background(self, line, tileNum):
        #tile num is right, then loading the tiles is wrong and the tiles aren't getting loaded to the correct
        #spot on the rect
        print("TileNum: " + tileNum)