import pygame
import math
import config

class SpriteSheet(object):
    #load spritesheet
    def __init_(self, file_name):

        self.spriteSheet = pygame.image.load(file_name).convert()

        #get width of tiles: width / pixel size of each tile
        self.tile_width = (self.spriteSheet.get_width()) / config.TILE_SIZE
        #get length of tiles
        self.tile_height = (self.spriteSheet.get_height()) / config.TILE_SIZE

    #get sprite
    def get_image(self, tileNum):
        #make a new image for sprite
        image = pygame.Surface([config.TILE_SIZE, config.TILE_SIZE]).convert_alpha()

        #copy the sprite from the sheet to the new image
        #to find the x:
        x = tileNum % (self.tile_width -1) * config.TILE_SIZE
        #to find the y: 
        y = math.floor(tileNum / self.tile_height) * config.TILE_SIZE
        #image.blit(self.spriteSheet, (0, 0), (x, y, config.TILE_SIZE, config.TILE_SIZE))

        #set transparent color to white
        image.set_colorkey(config.WHITE)

        return image

