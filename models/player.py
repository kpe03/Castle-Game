import pygame
from models.entity import Entity
from utils.spritesheet import CharSpriteSheet
from utils.animation import Animation
from utils.input import Input
from traits.move import Move, Walk

#todo: flexibility for character creation
spriteSheet = CharSpriteSheet()
walkAnimations = {
    #walk (each walk has an animation and idle animation)
    #todo: implement idle animations
    "walk-down": Animation([spriteSheet.get_image(17), spriteSheet.get_image(18), spriteSheet.get_image(19),
                           spriteSheet.get_image(20), spriteSheet.get_image(21), spriteSheet.get_image(22), spriteSheet.get_image(23)],
                           spriteSheet.get_image(1)),
    "walk-left": Animation([spriteSheet.get_image(25), spriteSheet.get_image(26), spriteSheet.get_image(27),
                           spriteSheet.get_image(27), spriteSheet.get_image(28), spriteSheet.get_image(29), spriteSheet.get_image(30)],
                           spriteSheet.get_image(9)),
    "walk-right": Animation([spriteSheet.get_image(33), spriteSheet.get_image(34), spriteSheet.get_image(35),
                           spriteSheet.get_image(36), spriteSheet.get_image(37), spriteSheet.get_image(38), spriteSheet.get_image(39)],
                           spriteSheet.get_image(14)),
    "walk-up": Animation([spriteSheet.get_image(41), spriteSheet.get_image(42), spriteSheet.get_image(43),
                           spriteSheet.get_image(44), spriteSheet.get_image(45), spriteSheet.get_image(46), spriteSheet.get_image(47)],
                           spriteSheet.get_image(4))
}

class Player(Entity):
    def __init__(self, position, screen):
        super(Player, self).__init__(position)
        self.input = Input(self) #player input
        self.screen = screen #blit sprites
        # traits of the player class
        self.traits = {
            #todo: make work with multiple animations?
            "walk": Walk(walkAnimations, self.screen, self)
        }

    #update players position + change sprites
    def updatePosition(self, x_pos, y_pos):
       #update position
       self.position[0] += x_pos
       self.position[1] += y_pos
       

    #to do: update using traits and animations
    def render(self, screen):
        screen.blit(spriteSheet.get_image(9), self.position)
        
    
    #handle rendering, position, collision, input
    def update(self):
        self.updateTraits()
        self.input.checkInput()
        
        

        