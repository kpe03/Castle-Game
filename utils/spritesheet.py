import pygame
import config

class SpriteSheet(object):
    #load spritesheet
    def __init_(self, file_name):

        self.spriteSheet = pygame.image.load(file_name).convert()

    #get sprite
    def get_image(self, x, y, width, height):
        #make a new image for sprite
        image = pygame.Surface([width, height]).convert()

        #copy the sprite from the sheet to the new image
        image.blit(self.spriteSheet, (0, 0), (x, y, width, height))

        #set transparent color to white
        image.set_colorkey(config.WHITE)

        return image

