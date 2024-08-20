import sys
import pygame

from pygame import Surface
from pygame.event import Event

from game_settings import Settings
from snake import Snake
from ui_handler import UIHandler
from scene_manager import SceneManager
from audio_handler import AudioHandler


def check_events(snake: Snake, ui: UIHandler, scene: SceneManager,
                 audio: AudioHandler) -> None:
    """
    Handle user input events.

    :param snake: the snake game object.
    :param ui: a reference to the ui handler.
    :param scene: a reference to the screen manager.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake, ui, scene, audio)
        elif not scene.game_screen_active and event.type == ui.BLINKEVENT:
            ui.play_current = next(ui.play_blinker)
        elif event.type == pygame.MOUSEBUTTONDOWN and \
              scene.start_screen_active:
            if ui.start_hover:
                scene.start_screen_active = False
                scene.game_screen_active = True


def check_keydown_events(event: Event, snake: Snake, ui: UIHandler,
                         scene: SceneManager, audio: AudioHandler) -> None:
    """
    Handle key presses.

    :param event: the input event.
    :param snake: the snake game object.
    :param ui: a reference to the ui handler.
    :param scene: a reference to the scene manager.
    """
    if scene.game_screen_active and not scene.game_paused:
        if event.key in (pygame.K_UP, pygame.K_w) and \
            (not snake.speed_y or snake.length == 1):
            ui.moving = True
            snake.speed_x = 0
            snake.speed_y = -snake.size
            audio.move_sound.play()
        elif event.key in (pygame.K_DOWN, pygame.K_s)and \
            (not snake.speed_y or snake.length == 1):
            ui.moving = True
            snake.speed_x = 0
            snake.speed_y = snake.size
            audio.move_sound.play()
        elif event.key in (pygame.K_RIGHT, pygame.K_d)and \
            (not snake.speed_x or snake.length == 1):
            ui.moving = True
            snake.speed_x = snake.size
            snake.speed_y = 0
            audio.move_sound.play()
        elif event.key in (pygame.K_LEFT, pygame.K_a) and \
            (not snake.speed_x or snake.length == 1):
            ui.moving = True
            snake.speed_x = -snake.size
            snake.speed_y = 0
            audio.move_sound.play()
    
    if event.key == pygame.K_ESCAPE and scene.game_screen_active:
        scene.game_paused = not scene.game_paused

    if scene.end_screen_active and event.key == pygame.K_p:
        reset_game(ui, scene, snake)


def reset_game(ui: UIHandler, scene: SceneManager, snake: Snake) -> None:
    """
    Reset the game.

    :param ui: a reference to the ui handler.
    :param scene: a reference to the scene manager.
    :param snake: the snake game object.
    """
    # reset the score
    ui.score = 0
    #reset the snake
    snake.reset_snake()
    # change scenes
    scene.end_screen_active = False
    scene.game_screen_active = True


def update_screen(settings: Settings, screen: Surface, ui: UIHandler,
                  scene: SceneManager, snake: Snake) -> None:
    """
    Update the screen.

    :param settings: the game settings.
    :param screen: the screen.
    :param ui: a reference to the ui handler.
    :param scene: a reference to the scene manager.
    :param snake: the snake game object.
    """
    screen.fill(settings.bg_color)
    ui.draw_ui()
    if scene.game_screen_active:
        snake.draw_snake()
    pygame.display.flip()