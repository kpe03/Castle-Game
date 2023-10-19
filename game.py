import pygame
import utils.config
from utils.game_state import GameState

class FarmingGame:
    def __init__(self, screen):
        
        self.screen = screen
        self.objects = []
        self.map = []
        self.game_state = GameState.NONE

    #for game logic
    # def _process_game_logic(self):
    #     #placeholder

    def _handle_input(self):
        #quit game (return key)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        #player movement


                
        

        