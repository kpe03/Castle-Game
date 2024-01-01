import pygame
import utils.config

class Move:
    def __init__(self, animation, screen, entity):
        self.animation = animation #most likely a dictionary of animations
        self.screen = screen
        self.entity = entity #of entity class
        

    def update(self):
        #if moving:
        self.animation.update()
        #if not moving:
        self.animation.idle()

    def updateAnimation(self, animation):
        self.animation = animation
        self.update()

    def drawEntity(self):
        self.screen.blit(self.animation.image, self.entity.position)

#handle multiple walking animations?
class Walk(Move):
    def __init__(self, animation, screen, entity):
        super(Walk, self).__init__(animation, screen, entity)
        self.direction_y = 0 #keeps track of what direction player is moving
        self.direction_x = 0
        self.move = False #flag for moving
        
        
    def update(self):
        #todo: idle animation
        #when not zero, update animation with corresponding walk
            
        if self.move == True:
            if self.direction_x == -1:
                self.entity.updatePosition([-1 * utils.config.WALK_SPEED, 0])
                
            elif self.direction_x == 1:
                self.entity.updatePosition([ utils.config.WALK_SPEED, 0])
                
            if self.direction_y == -1:
                self.entity.updatePosition([0, -1 *  utils.config.WALK_SPEED])
                
            elif self.direction_y == 1:
                self.entity.updatePosition([0,  utils.config.WALK_SPEED])
                
            self.animation.update()
        else:
            if self.direction_x == 0 and self.direction_y == 0:
                self.animation.idle()
                print("Idling")
            self.animation.update()
            #update and draw
        
        self.drawEntity()
    
    def render(self, image, screen):
        screen.blit(image, self.position)

    def test(self):
        print("created")

            
            
    

        