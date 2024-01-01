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
    def __init__(self, animation, screen, entity, direction):
        super(Walk, self).__init__(animation, screen, entity)
        self.direction_y = 0 #keeps track of what direction player is moving
        self.direction_x = 0
        self.direction = direction
        # self.move = False #flag for moving
        
        
    def update(self):
        #todo: idle animation
        #when not zero, update animation with corresponding walk
        if self.entity.state == 'moving':
            if self.entity.direction == "walk-left":
                self.entity.updatePosition([-1 * utils.config.WALK_SPEED, 0])
            elif self.entity.direction == "walk-up":
                self.entity.updatePosition([0, -1 *  utils.config.WALK_SPEED])
            elif self.entity.direction == "walk-down":
                 self.entity.updatePosition([0,  utils.config.WALK_SPEED])
            elif self.direction == "walk-right":
                self.entity.updatePosition([ utils.config.WALK_SPEED, 0])
            # elif self.direction_x == 1:
            #     self.entity.updatePosition([ utils.config.WALK_SPEED, 0])
        else:
            pass
            # if self.direction_y == -1:
            #     self.entity.updatePosition([0, -1 *  utils.config.WALK_SPEED])
                
            # elif self.direction_y == 1:
            #     self.entity.updatePosition([0,  utils.config.WALK_SPEED])
            # self.drawEntity()
        self.animation.update()
        self.drawEntity()

        
    
    def render(self, image, screen):
        screen.blit(image, self.position)

    def test(self):
        print("created")

            
            
    

        