import pygame
import math
import utils.config

class SpriteSheet:
    #load spritesheet
    def __init__(self, file_name):

        self.spriteSheet = pygame.image.load(file_name).convert()

        #get width of tiles: width / pixel size of each tile
        self.tile_width = (self.spriteSheet.get_width()) / utils.config.TILE_SIZE
        #get length of tiles
        self.tile_height = (self.spriteSheet.get_height()) / utils.config.TILE_SIZE

    #get sprite
    def get_image(self, tileNum):
        #make a new image for sprite
        image = pygame.Surface([utils.config.TILE_SIZE, utils.config.TILE_SIZE])

        #copy the sprite from the sheet to the new image
        #to find the x:
        x = tileNum % (self.tile_width -1) * utils.config.TILE_SIZE
        
        #to find the y: 
        y = math.floor(tileNum / self.tile_height) * utils.config.TILE_SIZE
        
        #prints... but needs to be bigger and only prints one tile?
        #image.blit(self.spriteSheet, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.TILE_SIZE))

        #set transparent color to white
        #image.set_colorkey(utils.config.WHITE)

        return image
    
    def test_image(self, x, y):
        #for testing
        #x and y are calculating correctly..?
        print("Found y: " + str(y))
        print("Found x:" + str(x))

