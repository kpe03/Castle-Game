from utils.spritesheet import SpriteSheet

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
                print(trait.type)
            except AttributeError:
               pass

    def getPosition(self):
        return self.position

