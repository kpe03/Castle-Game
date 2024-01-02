import pygame
from models.entity import Entity
from utils.spritesheet import CharSpriteSheet
from utils.animation import Animation
from utils.input import Input
from traits.move import Walk
import utils.config

class Player(Entity):
    def __init__(self, position, screen):
        #todo: flexibility for character creation
        self.spriteSheet = CharSpriteSheet()
        super(Player, self).__init__(position)
        
        #set up player input:
        self.input = Input(self) 
        self.input.setUpInput()

        self.screen = screen #blit sprites
        # traits of the player class
        self.animations = {
            #walk (each walk has an animation and idle animation)
            #todo: implement idle animations
            "walk-down": Animation([self.spriteSheet.get_image(16),self.spriteSheet.get_image(17), self.spriteSheet.get_image(18),
                           self.spriteSheet.get_image(19), self.spriteSheet.get_image(20), self.spriteSheet.get_image(21)], self.spriteSheet.get_image(0)),

            "walk-left": Animation([self.spriteSheet.get_image(24), self.spriteSheet.get_image(25), self.spriteSheet.get_image(26),
                           self.spriteSheet.get_image(27), self.spriteSheet.get_image(28),self.spriteSheet.get_image(29)], self.spriteSheet.get_image(8)),

            "walk-right": Animation([self.spriteSheet.get_image(32), self.spriteSheet.get_image(33), self.spriteSheet.get_image(34),
                           self.spriteSheet.get_image(35), self.spriteSheet.get_image(36), self.spriteSheet.get_image(37)], self.spriteSheet.get_image(13)),

            "walk-up": Animation([self.spriteSheet.get_image(40), self.spriteSheet.get_image(41), self.spriteSheet.get_image(42),
                           self.spriteSheet.get_image(43), self.spriteSheet.get_image(44), self.spriteSheet.get_image(45)], self.spriteSheet.get_image(3)),
            
            "default": Animation([self.spriteSheet.get_image(0), self.spriteSheet.get_image(1), self.spriteSheet.get_image(2)],
                                  self.spriteSheet.get_image(0))
        }
        self.traits = {
            #todo: make work with multiple animations?
            "walk-right": Walk(self.animations["walk-right"], self.screen, self, "walk-right"),
            "walk-left": Walk(self.animations["walk-left"], self.screen, self, "walk-left"),
            "walk-up": Walk(self.animations["walk-up"], self.screen, self, "walk-up"),
            "walk-down": Walk(self.animations["walk-down"], self.screen, self, "walk-down"),
        }

    #update players position + change sprites
    def updatePosition(self, coords):
       #update position
       self.position[0] += coords[0]
       self.position[1] += coords[1]
       
    # #to do: update using traits and animations
    # def render(self, image, screen):
    #     screen.blit(image, self.position)
        
    #handle rendering, position, collision, input
    def update(self):
        self.input.checkInput() #handle input in input class
        # self.updateTraits()     #for each trait in traits of player, update them
