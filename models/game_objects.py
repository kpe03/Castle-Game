import pygame
from utils.spritesheet import SpriteSheet

#parent class for objects in game
class GameObjects:
    def __init__(self, position, file_name):
        self.position = position #keep track of object position on screen
        #self.radius   #for collision?
        #self.velocity #moving speed for object
        self.sprite_sheet = SpriteSheet(file_name) #create a spritesheet for object (for drawing)
        
    #for getting tiles and drawing them to the screen
    def draw_object(self, surface, tileNum):
        #using tile name, load the image
        self.sprite = self.sprite_sheet.get_image(tileNum)
        #calculate the position to blit image to surface
        blit_position = self.position #probably use more later
        #blit to surface
        surface.blit(self.sprite, blit_position)

    #detect collision
    #def collides_with(self, object):

