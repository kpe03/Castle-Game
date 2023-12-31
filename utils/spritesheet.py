import pygame
import math
import utils.config

# =================
#  sprite sheet
# =================
class SpriteSheet:
    #load spritesheet
    def __init__(self, file_name):
        #todo: Update spritesheet loading
        # self.spriteSheet = pygame.image.load(file_name).convert()
        try:
            self.sheet = pygame.image.load(file_name)
            if not self.sheet.get_alpha():
                self.sheet.set_colorkey((0,0,0))
        except pygame.error:
            print("unable to load spritesheet image:", file_name)
        
        #get width of tiles: width / pixel size of each tile
        self.tile_width = (self.sheet.get_width()) / utils.config.TILE_SIZE
        #get length of tiles
        self.tile_height = (self.sheet.get_height()) / utils.config.TILE_SIZE


    #todo: change to load all sprites (thus each sprite is only loaded once!!)
    def loadSprites(self):
        pass

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
        image.blit(self.sheet, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.TILE_SIZE))
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
class CharSpriteSheet():
    #load char sprite sheet
    def __init__(self):
        #for transparency: convert_alpha() and pygame.SRCALPHA flag in self.image!
        self.sheet = pygame.image.load("./assets/charas/princess_sheet.png").convert_alpha()
        self.image = pygame.Surface([utils.config.TILE_SIZE, utils.config.CHAR_HEIGHT], pygame.SRCALPHA)
        
        self.tile_width = math.floor(self.sheet.get_width() / utils.config.TILE_SIZE)
        self.tile_height = math.floor(self.sheet.get_height() / (utils.config.TILE_SIZE * 2))

    #overload
    def get_image(self, tileNum):
        # char_image = pygame.Surface([utils.config.TILE_SIZE, utils.config.TILE_SIZE * 2])
        x = (tileNum % (self.tile_width - 1) * utils.config.TILE_SIZE) 
        y = (math.floor(tileNum / (self.tile_height))) * (utils.config.TILE_SIZE * 2)

        #blits the sprite onto new image. image is now a pygame.Rect
        self.image.blit(self.image, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.TILE_SIZE * 2))
        #image.blit(image, (0, 0))
        sizedImage = pygame.transform.scale(self.image, (utils.config.SCALE, utils.config.CH_HEIGHT_SCALE))

        return sizedImage
    