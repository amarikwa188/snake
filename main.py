import pygame
from pygame import Surface
from pygame.time import Clock

from game_settings import Settings
import game_functions as gf
from ui_handler import UIHandler
from snake import Snake


def run_game() -> None:
    pygame.init()
    settings: Settings = Settings()
    screen: Surface = pygame.display.set_mode((settings.screen_width,
                                               settings.screen_height))
    ui_handler: UIHandler = UIHandler(settings, screen)
    clock: Clock = pygame.time.Clock()


    snake: Snake = Snake(settings, screen, ui_handler)

    while True:
        clock.tick(snake.size//2)
        gf.check_events(snake)
        snake.update()
        gf.update_screen(settings, screen, ui_handler, snake)


if __name__ == "__main__":
    run_game()