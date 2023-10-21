import pygame
import utils.config
import utils.game_state
from utils.background import Background

class FarmingGame():
    def __init__(self, screen):
        #set the created screen (width and height in config)
        self.screen = screen
        self.objects = []
        self.map = []
        self.game_state = utils.game_state.GameState.NONE
        #initialize the background with the tilesheet
        self.background = Background("assets/free version/free.png", self.screen)

    def set_up(self):
        self.game_state = utils.game_state.GameState.RUNNING
        self.handle_input()
        #load map
        self.background.load_map("map1")

    def update(self):
        self.screen.fill(utils.config.BLACK)
        #render map
        self.background.render_map()

    def draw(self, screen):
        screen.fill(utils.config.BLACK)
    

    #for game logic
    # def _process_game_logic(self):
    #     #placeholder

    def handle_input(self):
        #quit game (return key)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        #player movement

    


                
        

        