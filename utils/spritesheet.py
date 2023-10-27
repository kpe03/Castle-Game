import pygame
import math
import utils.config

# =================
#  sprite sheet
# =================
class SpriteSheet:
    #load spritesheet
    def __init__(self, file_name):

        self.spriteSheet = pygame.image.load(file_name).convert()

        #get width of tiles: width / pixel size of each tile
        self.tile_width = (self.spriteSheet.get_width()) / utils.config.TILE_SIZE
        #get length of tiles
        self.tile_height = (self.spriteSheet.get_height()) / utils.config.TILE_SIZE

    #get sprite
    def get_image(self, tileNum):
        #make a new image for sprite
        image = pygame.Surface([utils.config.TILE_SIZE, utils.config.TILE_SIZE])

        #copy the sprite from the sheet to the new image
        #to find the x:
        x = tileNum % (self.tile_width -1) * utils.config.TILE_SIZE
        
        #to find the y: 
        y = math.floor(tileNum / self.tile_height) * utils.config.TILE_SIZE
        
        #blits the sprite onto new image
        image.blit(self.spriteSheet, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.TILE_SIZE))
        #resize the image
        sizedImage = pygame.transform.scale(image, (utils.config.SCALE, utils.config.SCALE))

        #return resized, new sprite @ TileNum
        return sizedImage
    
    def test_image(self, x, y):
        #for testing
        #x and y are calculating correctly..?
        print("Found y: " + str(y))
        print("Found x:" + str(x))

# =================
# char sprite sheet
# =================
#a class to handle char sprites which are formatted differently
class CharSpriteSheet(SpriteSheet):
    #load char sprite sheet
    def __init__(self, file_name, tile_width, tile_height):
        super().__init__(tile_width, tile_height)
        #ignore the border
        self.border = utils.config.SHEET_BORDER

        self.spriteSheet = pygame.image.load(file_name).convert()
    
    #overload
    def get_image(self, tileNum):
        #make a sprite image that is 16x32
        image = pygame.Surface([utils.config.TILE_SIZE, utils.config.TILE_SIZE])

        #to find the x:
        x = tileNum % ((self.tile_width + self.border) -1) * utils.config.TILE_SIZE
        #to find the y: 
        y = math.floor(tileNum / self.tile_height) * utils.config.TILE_SIZE
        #blits the sprite onto new image
        image.blit(self.spriteSheet, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.TILE_SIZE))
        #resize the image
        sizedImage = pygame.transform.scale(image, (utils.config.SCALE, utils.config.SCALE))

        return sizedImage