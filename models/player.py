import pygame
from models.entity import Entity
from utils.spritesheet import CharSpriteSheet
from utils.animation import Animation
from utils.input import Input
from traits.move import Walk

class Player(Entity):
    def __init__(self, position, screen):
        #todo: flexibility for character creation
        self.spriteSheet = CharSpriteSheet()
        super(Player, self).__init__(position)
        self.input = Input(self) #player input
        self.screen = screen #blit sprites
        # traits of the player class
        self.walkAnimations = {
            #walk (each walk has an animation and idle animation)
            #todo: implement idle animations
            "walk-down": Animation([self.spriteSheet.get_image(16),self.spriteSheet.get_image(17), self.spriteSheet.get_image(18),
                           self.spriteSheet.get_image(19), self.spriteSheet.get_image(20), self.spriteSheet.get_image(21)],
                           self.spriteSheet.get_image(0)),
            "walk-left": Animation([self.spriteSheet.get_image(24), self.spriteSheet.get_image(25), self.spriteSheet.get_image(26),
                           self.spriteSheet.get_image(27), self.spriteSheet.get_image(28),self.spriteSheet.get_image(29)],
                           self.spriteSheet.get_image(9)),
            "walk-right": Animation([self.spriteSheet.get_image(32), self.spriteSheet.get_image(33), self.spriteSheet.get_image(34),
                           self.spriteSheet.get_image(35), self.spriteSheet.get_image(36), self.spriteSheet.get_image(37)],
                           self.spriteSheet.get_image(14)),
            "walk-up": Animation([self.spriteSheet.get_image(40), self.spriteSheet.get_image(41), self.spriteSheet.get_image(42),
                           self.spriteSheet.get_image(43), self.spriteSheet.get_image(44), self.spriteSheet.get_image(45), self.spriteSheet.get_image(46)],
                           self.spriteSheet.get_image(4))
        }
        self.traits = {
            #todo: make work with multiple animations?
            "walk": Walk(self.walkAnimations, self.screen, self)
        }

    #update players position + change sprites
    def updatePosition(self, x_pos, y_pos):
       #update position
       self.position[0] += x_pos
       self.position[1] += y_pos
       
    #to do: update using traits and animations
    def render(self, image, screen):
        screen.blit(image, self.position)
        
    #handle rendering, position, collision, input
    def update(self):
        self.input.checkInput()
        self.updateTraits()
        #self.render(self.spriteSheet.get_image(15), self.screen)
        
        

        