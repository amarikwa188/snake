import pygame
from pygame import Surface
from pygame.time import Clock

from game_settings import Settings
import game_functions as gf
from ui_handler import UIHandler
from scene_manager import SceneManager
from audio_handler import AudioHandler
from snake import Snake


def run_game() -> None:
    pygame.init()
    pygame.display.set_caption("Snake")
    settings: Settings = Settings()
    screen: Surface = pygame.display.set_mode((settings.screen_width,
                                               settings.screen_height))
    scene_manager: SceneManager = SceneManager()
    ui_handler: UIHandler = UIHandler(settings, screen, scene_manager)
    audio_handler: AudioHandler = AudioHandler()
    clock: Clock = pygame.time.Clock()

    snake: Snake = Snake(settings, screen, ui_handler, scene_manager,
                         audio_handler)

    while True:
        clock.tick(snake.size)
        gf.check_events(snake, ui_handler, scene_manager)

        if scene_manager.game_screen_active	and not scene_manager.game_paused:
            snake.update()

        gf.update_screen(settings, screen, ui_handler, scene_manager, snake)


if __name__ == "__main__":
    run_game()