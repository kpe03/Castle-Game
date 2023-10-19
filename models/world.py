import pygame

import constants

#the parent class for loading parts of the world
#ex: background tiles, collision with bounds, etc...
class World():
    def __init__(self, player):
        player.position