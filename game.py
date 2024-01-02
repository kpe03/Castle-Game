import pygame
import utils.config
from utils.game_state import GameState
from utils.background import Background
from models.player import Player

class CastleGame():
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.map = []
        self.player = Player(utils.config.SCREEN_CENTER, self.screen)
        self.game_state = GameState.NONE
        #initialize the background with the tilesheet
        self.background = Background("assets/free version/free.png", self.screen)

    def set_up(self):
        self.game_state = GameState.RUNNING
        self.background.load_map("map1")

    def update(self):
        self.background.render_map(self.screen)
        self.player.update() #input handled in player class
    
    def handle_events(self):
        pass
      
           
                    
                

    


                
        

        