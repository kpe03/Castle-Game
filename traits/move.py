
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
        if self.direction_x != 0:
            if self.direction_x < 0:
                self.animation["walk-left"].update()
            else:
                self.animation["walk-right"].update()
        if self.direction_y != 0:
            if self.direction_y < 0:
                self.animation["walk-up"].update()
            else:
                self.animation["walk-down"].update()
        
    def updateAnimation(self, animation):
        self.animation = animation
        self.update()


            
            
    

        