import sys
import pygame

from pygame import Surface
from pygame.event import Event

from game_settings import Settings
from snake import Snake
from ui_handler import UIHandler
from scene_manager import SceneManager


def check_events(snake: Snake, ui: UIHandler, scene: SceneManager) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake, ui, scene)
        elif not scene.game_screen_active and event.type == ui.BLINKEVENT:
            ui.play_current = next(ui.play_blinker)


def check_keydown_events(event: Event, snake: Snake, ui: UIHandler,
                         scene: SceneManager) -> None:
    if not scene.game_paused:
        if event.key in (pygame.K_UP, pygame.K_w) and \
            (not snake.speed_y or snake.length == 1):
            ui.moving = True
            snake.speed_x = 0
            snake.speed_y = -snake.size
        elif event.key in (pygame.K_DOWN, pygame.K_s)and \
            (not snake.speed_y or snake.length == 1):
            ui.moving = True
            snake.speed_x = 0
            snake.speed_y = snake.size
        elif event.key in (pygame.K_RIGHT, pygame.K_d)and \
            (not snake.speed_x or snake.length == 1):
            ui.moving = True
            snake.speed_x = snake.size
            snake.speed_y = 0
        elif event.key in (pygame.K_LEFT, pygame.K_a) and \
            (not snake.speed_x or snake.length == 1):
            ui.moving = True
            snake.speed_x = -snake.size
            snake.speed_y = 0
    
    if event.key == pygame.K_ESCAPE and scene.game_screen_active:
        scene.game_paused = not scene.game_paused


def update_screen(settings: Settings, screen: Surface, ui: UIHandler,
                  scene: SceneManager, snake: Snake) -> None:
    screen.fill(settings.bg_color)
    ui.draw_ui()
    if scene.game_screen_active:
        snake.draw_snake()
    pygame.display.flip()