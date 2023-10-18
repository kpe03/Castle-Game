import pygame

class FarmingGame:
    def __init__(self):
        self.__init__pygame()
        self.screen = pygame.display.set_mode(1280, 720)
        self.screen.fill("purple")
        self.clock = pygame.time.Clock()

    #draw assets on the screen
    # def _draw(self):
    #     #placeholder

    #for game logic
    # def _process_game_logic(self):
    #     #placeholder

    def _handle_input(self):
        #quit game (return key)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        #player movement

        