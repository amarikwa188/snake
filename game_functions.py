import sys
import pygame

from pygame import Surface
from pygame.event import Event

from game_settings import Settings
from snake import Snake
from ui_handler import UIHandler


def check_events(snake: Snake) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)


def check_keydown_events(event: Event, snake: Snake) -> None:
    if event.key in (pygame.K_UP, pygame.K_w) and not snake.speed_y:
        snake.speed_x = 0
        snake.speed_y = -snake.size
    elif event.key in (pygame.K_DOWN, pygame.K_s)and not snake.speed_y:
        snake.speed_x = 0
        snake.speed_y = snake.size
    elif event.key in (pygame.K_RIGHT, pygame.K_d)and not snake.speed_x:
        snake.speed_x = snake.size
        snake.speed_y = 0
    elif event.key in (pygame.K_LEFT, pygame.K_a) and not snake.speed_x:
        snake.speed_x = -snake.size
        snake.speed_y = 0


def update_screen(settings: Settings, screen: Surface, ui: UIHandler,
                  snake: Snake) -> None:
    screen.fill(settings.bg_color)
    ui.draw_ui()
    snake.draw_snake()
    pygame.display.flip()