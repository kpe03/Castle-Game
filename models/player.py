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
        self.input = Input(self) #player input
        self.screen = screen #blit sprites
        self.state = 'resting' #determines state of player
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
        self.states = {
            "resting": self.resting,
            "moving": self.moving,
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
        self.input.checkInput()
        # self.updateTraits()
        #self.render(self.spriteSheet.get_image(15), self.screen)

    #handle movement of player -------------------------------------------------------
    def begin_moving(self, direction):
        self.direction = self.traits[direction] #update animation using dictionary
        self.state = "moving" #starts moving the sprite
        
    def moving(self):
        #update position
        if self.entity.direction == "walk-left":
            self.updatePosition([-1 * utils.config.WALK_SPEED, 0])
        elif self.entity.direction == "walk-up":
            self.updatePosition([0, -1 *  utils.config.WALK_SPEED])
        elif self.entity.direction == "walk-down":
            self.updatePosition([0,  utils.config.WALK_SPEED])
        elif self.direction == "walk-right":
            self.updatePosition([utils.config.WALK_SPEED, 0])

        self.traits[self.direction].update() #update corresponding animation

    def begin_resting(self, direction):
        self.state = "resting"
        self.direction = direction

    #when player is not moving
    def resting(self):
        self.animations[self.direction].idle()

    def drawEntity(self):
        self.screen.blit(self.anmiation.image, self.position)