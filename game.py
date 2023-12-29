import pygame
import utils.config
from utils.game_state import GameState
from utils.background import Background
from models.player import Player

class CastleGame():
    def __init__(self, screen):
        #set the created screen (width and height in config)
        self.screen = screen
        self.objects = []
        self.map = []
        self.game_state = GameState.NONE
        #initialize the background with the tilesheet
        self.background = Background("assets/free version/free.png", self.screen)

    def set_up(self):
        #load player in the center of the screen and sprite sheet
        player = Player(utils.config.SCREEN_CENTER, "assets/charas/princess_sheet.png")
        self.player = player

        #other:
        self.game_state = GameState.RUNNING
        #load map
        self.background.load_map("map1")
        #render map to screen

    def update(self):
        self.handle_input()
        #update screen
        self.background.render_map(self.screen)
        self.player.render(self.screen, 0)
    
    #for game logic
    # def _process_game_logic(self):
    #     #placeholder

    def handle_input(self):
        #quit game (return key)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            #player movement:
            #move while key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: #up
                    self.player.update_position(0 , -1)
                elif event.key == pygame.K_s: #down
                    self.player.update_position(0 , 1)
                elif event.key == pygame.K_a: #left
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_d: #right
                    self.player.update_position(1, 0)
                    
                

    


                
        

        