import pygame
import utils.config
from utils.game_state import GameState
from utils.background import Background
from utils.input import Input
from models.player import Player

class CastleGame():
    def __init__(self, screen):
        #set the created screen (width and height in config)
        
        self.screen = screen
        self.objects = []
        self.map = []
        self.player = Player(utils.config.SCREEN_CENTER, self.screen)
        self.game_state = GameState.NONE
        #initialize the background with the tilesheet
        self.background = Background("assets/free version/free.png", self.screen)

    def set_up(self):
        #load player in the center of the screen and sprite sheet
        self.game_state = GameState.RUNNING
        #load map
        self.background.load_map("map1")

    def update(self):
        #update screen
        self.background.render_map(self.screen)
        self.player.update()
        # utils.input.checkInput() #checks input events
    
    def handle_events(self):
        pass
      
           
                    
                

    


                
        

        