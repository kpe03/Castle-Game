import math
"""utils: file for loading backgrounds and other objects"""
#for now: a list made from .txt map
#find a better way to integrate it 
map_tile_image = {
     
}

#load maps from /maps 
#reads from .txt file and converts to a list
def load_map(self, file_name):
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles =[]
                for i in range(0, len(line) -1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            print(self.map)

#using list, get tiles from spritesheet
# def render_map(self, screen):
#     y_pos = 0
#     for line in self.map:
#         x_pos = 0
#         for tile in line:
#             image = map_tile_image[tile]
#             rect = pygame.Rect(x_pos * utils.config.SCALE, y_pos * utils.config.SCALE,
#                             utils.config.SCALE, utils.config.SCALE)