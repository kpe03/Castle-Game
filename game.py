import pygame
import utils.config
from utils.game_state import GameState
from utils.background import Background
from models.player import Player

class CastleGame():
    def __init__(self, screen):
        #set the created screen (width and height in config)
        self.x_move = 0
        self.y_move = 0
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
        self.game_state = GameState.RUNNING
        #load map
        self.background.load_map("map1")

    def update(self):
        #update screen
        self.background.render_map(self.screen)
        self.player.render(self.screen, 0)
        self.handle_events()
    
    def handle_events(self):
        #key events only occur one at a time
        #keep values for each event and only change when key goes up or down.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            #player movement:
            ## KEYDOWN triggers when keys are released movement continues
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: #up
                    self.y_move = -1
                elif event.key == pygame.K_s: #down
                    self.y_move = 1
                elif event.key == pygame.K_a: #left
                    self.x_move = -1
                elif event.key == pygame.K_d: #right  
                    self.x_move = 1
            ## KEYUP triggers when keys are released, movement stops
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: #up
                    self.y_move = 0
                elif event.key == pygame.K_s: #down
                    self.y_move = 0
                elif event.key == pygame.K_a: #left
                    self.x_move = 0
                elif event.key == pygame.K_d: #right  
                    self.x_move = 0
            print(self.x_move, self.y_move)
            #update positions for each event
            self.player.update_position(self.x_move, self.y_move)
            self.player.update_position(self.x_move, self.y_move)
           
                    
                

    


                
        

        