
class Move:
    def __init__(self, animation, screen, entity):
        self.animation = animation
        self.screen = screen
        self.entity = entity

    def update(self):
        #if moving:
        self.animation.update()
        #if not moving:
        self.animation.idle()

    def updateAnimation(self, animation):
        self.animation = animation
        self.update()

    def drawEntity(self):
        self.screen.blit(self.animation.image, self.entity.getPos())

#handle multiple walking animations?
class Walk:
    def __init__(self, animation, screen, entity):
        super(Move, self).__init__(animation, screen, entity)

        