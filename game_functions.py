import sys
import pygame


def check_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen() -> None:
    pygame.display.flip()