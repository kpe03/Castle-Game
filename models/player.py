import pygame
import collections

import utils.config
from models.game_objects import GameObjects
from utils.spritesheet import SpriteSheet

class Player(GameObjects):
    def __init__(self, position, file_name):
        super().__init__(position)
        self.charSprite = SpriteSheet(file_name) #load spritesheet for image
        self.rect = pygame.Rect() #for sprites
        #customizable things ------
        #self.hair sprite object for hair?
        #self.shirt sprite object for shirt
        #self.bottoms sprite object for pants
        #self.shoes sprite object for shoes
        #self.hat sprite object for hat
        #----------------------------
        #self.animations_list = [] #for later: list of animations

    #update players position + change sprites
    def update_position(self, new_position, tileNumList):
       #update position
       #depending on x,y coords, change the direction of movement?
        self.position += new_position
        
    #grabs the tile from the spritesheet
    def load_sprites(self, tileNumList):
        #get each tileNum in the tuple
        for tile in tileNumList:
            #the first tile will be the head of the player sprite
            self.charSprite.get_image(tile)
        
    #blit to screen at current position
    def render(self, screen, tileNumList):
        screen.blit(self.charSprite(tileNum), self.position)

    

