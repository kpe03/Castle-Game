import pygame

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
        self.animation.deltaTime = 6
        if self.move == True:
            self.animation.update()
            self.drawEntity()
        #idle animation
        else:
            #self.drawEntity()
            pass
     
    def render(self, image, screen):
        screen.blit(image, self.position)

            
            
    

        