

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
        

    def update(self):
        #todo: idle animation for each walk?
        #when not zero, update animation with corresponding walk
        self.animation.deltaTime = 6

        if self.direction_x == 1:
            pass
        elif self.direction_x == -1:
            pass
        if self.direction_x == 0 and self.direction_y == 0:
            self.animation = self.entity.walkAnimations["default"]
        self.animation.update()
        self.drawEntity()
        # print(self.direction_x)
        # if self.direction_x != 0:
        #     if self.direction_x < 0:
        #         self.animation = self.entity.walkAnimations["walk-left"]
        #         self.animation.update()
        #         self.drawEntity()
        #         # self.entity.position[0] += -1
        #     elif self.direction_y > 0:
        #         self.animation = self.entity.walkAnimations["walk-right"]
        #         self.animation.update()
        #         self.drawEntity()
                # self.entity.position[0] += 1
            
        
        
        # print(self.animation.image, self.position.entity)
        
        # if self.direction_y != 0:
        #     if self.direction_y < 0:
        #         self.animation["walk-up"].update()
        #         self.entity.position[1] += -1
        #     else:
        #         self.animation["walk-down"].update()
        #         self.entity.position[1] += 1
    def render(self, image, screen):
        screen.blit(image, self.position)

            
            
    

        