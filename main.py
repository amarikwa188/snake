import pygame
from pygame import Surface

from game_settings import Settings


def run_game() -> None:
    pygame.init()
    settings: Settings = Settings()
    screen: Surface = pygame.display.set_mode((settings.screen_width,
                                               settings.screen_height))
    
    while True:
        pass


if __name__ == "__main__":
    run_game()