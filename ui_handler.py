import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game_settings import Settings


class UIHandler:
    def __init__(self, settings: Settings, screen: Surface) -> None:
        self.settings: Settings = settings
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # self.score_font_single: Font = pygame.font.\
        #     Font("fonts/ARCADE.TTF", 300)
        self.score_font_single: Font = pygame.font.\
            SysFont(None, 300)
        # self.score_font_double: Font = pygame.font.\
        #     Font("fonts/ARCADE.TTF", 260)
        self.score_font_double: Font = pygame.font.\
             SysFont(None, 260)
        self.score_color: tuple[int,int,int] = self.settings.score_color

        self.score: int = 0


    def draw_ui(self) -> None:
        self.display_score()


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