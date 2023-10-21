import pygame
import utils.config
import utils.game_state

from game import FarmingGame

pygame.init()

#create the screen
screen = pygame.display.set_mode((utils.config.SCREEN_WIDTH, utils.config.SCREEN_HEIGHT))

pygame.display.set_caption("Farming Game")

clock = pygame.time.Clock()

game = FarmingGame(screen)
#call methods for starting game, input/logic, and drawing to screen
game.set_up()

while game.game_state == utils.game_state.GameState.RUNNING:
    clock.tick(60)
    game.update()
    pygame.display.flip()
