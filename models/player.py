import pygame
from models.game_objects import GameObjects
from utils.spritesheet import SpriteSheet

class Player(GameObjects):
    def __init__(self, position, file_name):
        super().__init__(position)
        self.sprite_sheet = SpriteSheet(file_name) #load spritesheet for image
        
    

