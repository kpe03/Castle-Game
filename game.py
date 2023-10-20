import pygame
import utils.config
from utils.game_state import GameState
from utils.background import load_map, render_map

class FarmingGame:
    def __init__(self, screen):
        
        self.screen = screen
        self.objects = []
        self.map = []
        self.game_state = GameState.NONE

    def set_up(self):
        self.game_state = GameState.RUNNING
        self.handle_input()

        self.load_map("01")

    def update(self):
        self.screen.fill(utils.config.BLACK)

        self.render_map(self.screen)

    #for game logic
    # def _process_game_logic(self):
    #     #placeholder

    def handle_input(self):
        #quit game (return key)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        #player movement

    


                
        

        