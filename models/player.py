import pygame
import collections

import utils.config
from models.game_objects import GameObjects
from utils.spritesheet import SpriteSheet

class Player(GameObjects):
    def __init__(self, position, file_name):
        super().__init__(position)
        self.sprite_sheet = SpriteSheet(file_name) #load spritesheet for image
        self.rect = pygame.Rect() #for sprites
        #self.animations_list = [] #for later: list of animations

    #update players position + change sprites
    def update_position(self, new_position, tile_Num):
        #position is a tuple, thus we can add the new position to the old one
        #remember!! tuples are not mutable!!!
        self.position += new_position
        
        #side note: [] are lists thus their items are strings
        #(1, 1) is a tuple thus type(1) would be 'int'

    def load_sprites(self, tileNum):
        return self.sprite_sheet.get_image(tileNum)
           
    #make a call to load_sprites to get the current one
    #blit to screen at current position
    def render(self, screen, tileNum):
        screen.blit(self.load_sprites(tileNum), self.position)

    

