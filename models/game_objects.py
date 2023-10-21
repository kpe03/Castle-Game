import pygame

#parent class for objects in game
class GameObjects:
    def __init__(self, position):
        self.position #may not need this?
        self.radius   #for collision?
        self.velocity #moving speed for object
        self.sprite #sprite for object