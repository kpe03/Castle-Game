import pygame
from utils.spritesheet import SpriteSheet

#parent class for objects in game
class Entity:
    #todo: add attributes to entity class
    def __init__(self, position):
        self.position = position #list with x, y coord
        self.traits = None
        #self.radius

    #process all the traits of characters  
    def updateTraits(self):
        for trait in self.traits.values():
            try:
                trait.update()
            except AttributeError:
                pass

    #for getting tiles and drawing them to the screen
    # def draw_object(self, surface, tileNum):
    #     #using tile name, load the image
    #     self.sprite = self.sprite_sheet.get_image(tileNum)
        #calculate the position to blit image to surface
       # blit_position = self.position #probably use more later
        #blit to surface
        #surface.blit(self.sprite, blit_position)

    #detect collision
    #def collides_with(self, object):
