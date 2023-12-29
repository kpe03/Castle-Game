import pygame

from models.game_objects import GameObjects
from utils.spritesheet import CharSpriteSheet
from utils.input import Input

class Player(GameObjects):
    def __init__(self, position, file_name, screen):
        super().__init__(position, file_name)
        self.charSprite = CharSpriteSheet(file_name) #load spritesheet for image
        self.position = position
        self.input = Input(self) #player input
        self.screen = screen #blit sprites

    #update players position + change sprites
    def updatePosition(self, x_pos, y_pos):
       #update position
       self.position[0] += x_pos
       self.position[1] += y_pos

    #blit to screen at current position
    def render(self, screen, tileNum):
        image = self.charSprite.get_image(tileNum)
        screen.blit(image, self.position)
    
    #handle rendering, position, collision, input
    def update(self):
        self.input.checkInput()
        self.render(self.screen, 0)
