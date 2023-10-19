import pygame
import utils.config
from utils.game_state import GameState

from game import FarmingGame

pygame.init()

screen = pygame.display.set_mode((utils.config.SCREEN_WITH, utils.config.SCREEN_HEIGHT))

pygame.display.set_caption("Farming Game")

clock = pygame.time.Clock()

game = FarmingGame(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(60)
    game.update()
    pygame.display.flip()
