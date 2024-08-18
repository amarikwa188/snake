import sys
import pygame

from pygame import Surface
from game_settings import Settings
from snake import Snake

from pygame.event import Event


def check_events(snake: Snake) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)


def check_keydown_events(event: Event, snake: Snake) -> None:
    if event.key == pygame.K_UP and not snake.speed_y:
        snake.speed_x = 0
        snake.speed_y = -snake.size
    elif event.key == pygame.K_DOWN and not snake.speed_y:
        snake.speed_x = 0
        snake.speed_y = snake.size
    elif event.key == pygame.K_RIGHT and not snake.speed_x:
        snake.speed_x = snake.size
        snake.speed_y = 0
    elif event.key == pygame.K_LEFT and not snake.speed_x:
        snake.speed_x = -snake.size
        snake.speed_y = 0


def update_screen(settings: Settings, screen: Surface, snake: Snake) -> None:
    screen.fill(settings.bg_color)
    snake.draw_snake()
    pygame.display.flip()