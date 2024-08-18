import pygame
from pygame import Surface, Rect
from pygame.font import Font

from itertools import cycle

from game_settings import Settings
from scene_manager import SceneManager


class UIHandler:
    def __init__(self, settings: Settings, screen: Surface, 
                 scene: SceneManager) -> None:
        self.settings: Settings = settings
        self.scene: SceneManager = scene
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.score_font_single: Font = pygame.font.\
            SysFont(None, 300)
        self.score_font_double: Font = pygame.font.\
             SysFont(None, 260)
        self.instructions_font: Font = pygame.font.\
            SysFont(None, 50)
        self.score_color: tuple[int,int,int] = self.settings.score_color

        self.game_over_font: Font = pygame.font.SysFont(None, 60)
        self.final_score_font: Font = pygame.font.SysFont(None, 35)
        self.blinker_font: Font = pygame.font.SysFont(None, 30)

        self.score: int = 0
        self.moving: bool = False

        # handle blinking text
        self.BLINKEVENT: int = pygame.USEREVENT + 1

        play_text: str = "Press P to play again..."
        self.play_blinker, self.play_rect = self.blinker(play_text)
        self.play_current: Surface = next(self.play_blinker)


    def draw_ui(self) -> None:
        if self.scene.game_screen_active:
            self.game_display()

        if self.scene.end_screen_active:
            self.end_screen_display()
            self.screen.blit(self.play_current, self.play_rect)


    def game_display(self) -> None:
        if self.moving:
            self.display_score()
        else:
            self.display_instructions()


    def display_score(self) -> None:
        if self.score < 10:
            image: Surface = self.score_font_single.render(f"{self.score}",
                                                           True,
                                                           self.score_color)
        else:
            image = self.score_font_double.render(f"{self.score}", True,
                                                  self.score_color)

        image.set_alpha(180)
        image_rect: Rect = image.get_rect()

        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = self.screen_rect.centery + 10

        self.screen.blit(image, image_rect)


    def display_instructions(self) -> None:
        text1: str = "Use Arrow Keys"
        text2: str = "to Move"
        image1: Surface = self.instructions_font.render(text1, True,
                                                       self.score_color)
        image1_rect: Rect = image1.get_rect()

        image1_rect.centerx = self.screen_rect.centerx
        image1_rect.centery = self.screen_rect.centery-20

        image2: Surface = self.instructions_font.render(text2, True,
                                                       self.score_color)
        image2_rect: Rect = image2.get_rect()

        image2_rect.centerx = self.screen_rect.centerx
        image2_rect.centery = self.screen_rect.centery+20

        self.screen.blit(image1, image1_rect)
        self.screen.blit(image2, image2_rect)


    def end_screen_display(self) -> None:
        self.display_game_over()


    def display_game_over(self) -> None:
        text: str = "GAME OVER"
        image: Surface = self.game_over_font.render(text, True, (0,0,0))
        image_rect: Rect = image.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = 55

        self.screen.blit(image, image_rect)

        score: str = f"Final Score: {self.score}"
        image2: Surface = self.final_score_font.render(score, True, 
                                                       (0,0,0))
        image2_rect: Rect = image2.get_rect()
        image2_rect.centerx = self.screen_rect.centerx
        image2_rect.centery = 100

        self.screen.blit(image2, image2_rect)
    

    def blinker(self, text: str) -> tuple[cycle, Rect]:
        image1: Surface = self.blinker_font.render(text, True, (0,0,0))
        image2: Surface = image1.copy()
        image2.set_alpha(100)

        image_rect: Rect = image1.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = 160
        blinker: cycle = cycle([image1, image2])

        return blinker, image_rect
