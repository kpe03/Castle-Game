import pygame

class Animation:
    def __init__(self, images, idleSprite=None, deltaTime=6):
        self.images = images
        self.index = 0 #index of current image of animation
        self.time = 0 #to cycle thro images
        self.image = self.images[self.index]
        self.deltaTime = deltaTime
        self.idleSprite = idleSprite #none by default

    #update frames of animation
    def update(self):
        self.timer += 1
        if self.timer % self.deltaTime == 0:
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                self.index = 0
        self.image = self.images[self.index]

    def idle(self):
        self.image = self.idleSprite