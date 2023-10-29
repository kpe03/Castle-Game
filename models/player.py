import pygame

from models.game_objects import GameObjects
from utils.spritesheet import CharSpriteSheet, SpriteSheet

class Player(GameObjects):
    def __init__(self, position, file_name):
        super().__init__(position, file_name)
        self.charSprite = CharSpriteSheet(file_name) #load spritesheet for image
        self.position = position
        #self.rect = pygame.Rect() #for sprites
        #customizable things ------
        #self.hair sprite object for hair?
        #self.shirt sprite object for shirt
        #self.bottoms sprite object for pants
        #self.shoes sprite object for shoes
        #self.hat sprite object for hat
        #----------------------------
        #self.animations_list = [] #for later: list of animations

    #update players position + change sprites
    def update_position(self, x_pos, y_pos):
       #update position
       self.position[0] += x_pos
       self.position[1] += y_pos

    #grabs the tile from the spritesheet
    # def load_sprites(self, tileNum):
        #get each tileNum in the tuple
        #the first tile will be the head of the player sprite
        # self.charSprite.get_image(tileNum)
        
    #blit to screen at current position
    def render(self, screen, tileNum):
        #print("player rendered")
        image = self.charSprite.get_image(tileNum)
        print(self.position)
        screen.blit(image, self.position)
        

    

