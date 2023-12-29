import pygame

from models.game_objects import GameObjects
from utils.spritesheet import CharSpriteSheet

class Player(GameObjects):
    def __init__(self, position, file_name):
        super().__init__(position, file_name)
        self.charSprite = CharSpriteSheet(file_name) #load spritesheet for image
        self.position = position
        

    #update players position + change sprites
    def update_position(self, x_pos, y_pos):
       #update position
       self.position[0] += x_pos
       self.position[1] += y_pos

    #blit to screen at current position
    def render(self, screen, tileNum):
        image = self.charSprite.get_image(tileNum)
        print(self.position)
        screen.blit(image, self.position)
        

    

