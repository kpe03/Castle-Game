import pygame
import utils.config
from utils.game_state import GameState
from utils.background import Background
from models.player import Player

class FarmingGame():
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
        player = Player(utils.config.SCREEN_CENTER, "assets/char free/global.png")
        self.player = player

        #other:
        self.game_state = GameState.RUNNING
        #load map
        self.background.load_map("map1")

    def update(self):
        self.handle_input()
        #update screen
        self.background.render_map(self.screen)
        #draw sprites based on position/direction
        #change render so that tile is not passed. 
        self.player.render(self.screen)
    
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
        keys = pygame.key.get_pressed()
        if self.player:
            if keys[pygame.K_w]: #up
                self.player.update_position(0 , -1 * utils.config.WALK_SPEED)
            elif keys[pygame.K_s]: #down
                self.player.update_position(0 , utils.config.WALK_SPEED)
            elif keys[pygame.K_a]: #left
                self.player.update_position(-1 * utils.config.WALK_SPEED, 0)
            elif keys[pygame.K_d]: #right
                self.player.update_position(utils.config.WALK_SPEED, 0)

                

    


                
        

        