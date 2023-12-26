import pygame
import math
import utils.config

# =======================================
#            sprite sheet
# =======================================
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

# ===========================================
#           char sprite sheet
# ===========================================
#a class to handle char sprites which are formatted differently
class CharSpriteSheet(SpriteSheet):
    #load char sprite sheet
    def __init__(self, file_name):
        super().__init__(file_name)
        #for transparency: convert_alpha() and pygame.SRCALPHA flag in self.image!
        self.spriteSheet = pygame.image.load(file_name).convert_alpha()
        #make a sprite image that is 16x32
        self.image = pygame.Surface([utils.config.TILE_SIZE, utils.config.CHAR_HEIGHT], pygame.SRCALPHA)
        
    def get_image(self, tileNum):
        #tileNums are based on 16x16 squares. would be cool if it could be 16x24 tiles...

        #must account for the 8 px border around spritesheet
        x = (tileNum % (self.tile_width - 1) * utils.config.TILE_SIZE) + utils.config.SHEET_BORDER
        #idk why this works but its does.
        #divide tilenum  by 24/tile_height and multiply by 32/tile_size*2. then add 8px border
        y = (math.floor(tileNum / self.tile_height) * 32) + utils.config.SHEET_BORDER
        
        #blit and resize image
        self.image.blit(self.spriteSheet, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.CHAR_HEIGHT))
        self.image.blit(self.image, (0,0))

        
        sizedImage = pygame.transform.scale(self.image, (utils.config.SCALE, utils.config.CH_HEIGHT_SCALE))
    
        return sizedImage
    
    
    def get_accessories(self, tileNum):
        x = x = (tileNum % (self.tile_width - 1) * utils.config.TILE_SIZE) + utils.config.SHEET_BORDER