import pygame

from models.game_objects import GameObjects
from utils.spritesheet import CharSpriteSheet, SpriteSheet

class Player(GameObjects):
    def __init__(self, position, file_name):
        super().__init__(position, file_name)
        self.charSprite = CharSpriteSheet(file_name) #load spritesheet for image
        self.position = position #default: center of screen
        self.direction = 0  #default: 0

        #customizable things
        self.objects = []
        #self.hair sprite object for hair?
        #self.shirt sprite object for shirt
        #self.bottoms sprite object for pants
        #self.shoes sprite object for shoes
        #self.hat sprite object for hat

        #self.animations_list = [] #for later: list of animations

    #update players position + change sprites
    def update_position(self, x_pos, y_pos):
       #update position 
       self.position[0] += x_pos
       self.position[1] += y_pos

       #when position updates change direction of the player
       #moving right
       if x_pos > 0:
           self.direction = 1
       elif x_pos < 0:
           self.direction = -1
        
    #blit to screen at current position
    def render(self, screen, counter):
        #list of animation tiles:
        walkAnimR = [0, 2, 4, 6, 8, 10, 12, 14]
        walkAnimL = [45, 47, 49, 51, 53, 55, 57, 59]
        tileNum = 0
        #standing/no movement
        print(tileNum)
        if self.direction == 1:
            image = self.charSprite.get_image(walkAnimR[counter])
        elif self.direction == -1:
            image = self.charSprite.get_image(walkAnimL[counter])

        #tileNums are based on 16x16 squares
        screen.blit(image, self.position)
        

    

