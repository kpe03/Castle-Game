from utils.animation import Animation
from utils.spritesheet import SpriteSheet

#todo:
# optimize spritesheet loading
class Sprites:
    def __init__(self):
        #load all sprite sheets
        self.backgroundSprites = self.loadSprites(
            [
                "./assets/free version/free.png",

            ]
        ),
        self.modelsSprites = self.loadSprites(
            [
                "./assets/charas/princess_sheet.png",
            ]
        )
        

    def loadBackgroundSprites(self, file_list):
        for file in file_list:
            with open(file):
                mySpritesheet = SpriteSheet(file)
                dic = {}

    #load all sprites
    #get height/width and get each possbile sprite
    #return dictionary w/ sprite tilenum
    def loadSprites(self, file_list):
        for file in file_list:
            with open(file):
                mySpritesheet = SpriteSheet(file)

                
