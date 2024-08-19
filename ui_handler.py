import pygame
from pygame import Surface, Rect
from pygame.font import Font

from itertools import cycle

from game_settings import Settings
from scene_manager import SceneManager


class UIHandler:
    """Represents an instance of the ui manager."""
    def __init__(self, settings: Settings, screen: Surface, 
                 scene: SceneManager) -> None:
        """
        Initializes a ui handler object.

        :param settings: the game settings
        :param screen: a reference to the game screen.
        :param scene: a reference to the scene manager.
        """
        # set up reference to the settings, screen and scene manager.
        self.settings: Settings = settings
        self.scene: SceneManager = scene
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # set up fonts and text colors
        self.score_font_single: Font = pygame.font.\
            SysFont(None, 300)
        self.score_font_double: Font = pygame.font.\
             SysFont(None, 260)
        self.instructions_font: Font = pygame.font.\
            SysFont(None, 50)
        self.score_color: tuple[int,int,int] = self.settings.score_color

        menu_font: str = "Courier New"
        self.game_over_font: Font = pygame.font.SysFont(menu_font, 45)
        self.final_score_font: Font = pygame.font.SysFont(menu_font, 18)
        self.blinker_font: Font = pygame.font.SysFont(menu_font, 15)

        # keep track of the score and whether the snake has started movings
        self.score: int = 0
        self.highscore: int  = 0
        self.moving: bool = False

        # handle blinking text
        self.BLINKEVENT: int = pygame.USEREVENT + 1

        play_text: str = "Press P to play again..."
        self.play_blinker, self.play_rect = self.blinker(play_text)
        self.play_current: Surface = next(self.play_blinker)


    def draw_ui(self) -> None:
        """
        Draw the ui to the screen.
        """
        # game screen
        if self.scene.game_screen_active:
            self.game_display()

        # end screen
        if self.scene.end_screen_active:
            self.display_game_over()
            self.screen.blit(self.play_current, self.play_rect)


    def game_display(self) -> None:
        """
        Handle the ui elements of the main gameplay screen.
        """
        if self.moving:
            self.display_score()
        else:
            self.display_instructions()


    def display_score(self) -> None:
        """
        Display the current score in the background of the game.
        """
        # adjust font size base on number of digits.
        if self.score < 10:
            image: Surface = self.score_font_single.render(f"{self.score}",
                                                           True,
                                                           self.score_color)
        else:
            image = self.score_font_double.render(f"{self.score}", True,
                                                  self.score_color)

        # lower the opacity
        image.set_alpha(180)

        # position the text
        image_rect: Rect = image.get_rect()

        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = self.screen_rect.centery + 10

        # render the text to the screen
        self.screen.blit(image, image_rect)


    def display_instructions(self) -> None:
        """
        Display movement instructions in place of the score at the
        start of the game.
        """
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


    def display_game_over(self) -> None:
        """
        Display a game over message and the final score on the end screen.
        """
        text: str = "GAME OVER"
        image: Surface = self.game_over_font.render(text, True, (0,0,0))
        image_rect: Rect = image.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = 50

        self.screen.blit(image, image_rect)

        score: str = f"Final Score: {self.score}"
        image2: Surface = self.final_score_font.render(score, True, 
                                                       (0,0,0))
        image2_rect: Rect = image2.get_rect()
        image2_rect.centerx = self.screen_rect.centerx
        image2_rect.centery = 95

        self.screen.blit(image2, image2_rect)

        highscore: str = f"High Score: {self.highscore}"
        image3: Surface = self.final_score_font.render(highscore, True,
                                                       (0,0,0))
        image3_rect: Rect = image3.get_rect()
        image3_rect.centerx = self.screen_rect.centerx
        image3_rect.centery = 120

        self.screen.blit(image3, image3_rect)
    

    def blinker(self, text: str) -> tuple[cycle, Rect]:
        """
        Create a cycle object to alternate between text displayed at a higher
        and lower opacity. Used for blinking text. Return both the blinker
        and the Rect where the text will be rendered.

        :param text: the text to be rendered
        :return: a tuple containing a cycle object and a rect.
        """
        # create the text surfaces
        image1: Surface = self.blinker_font.render(text, True, (0,0,0))
        image2: Surface = image1.copy()

        # lower the opacity of the second text surface
        image2.set_alpha(100)

        # create a Rect and position it appropriately
        image_rect: Rect = image1.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = 160

        # create the cycle object
        blinker: cycle = cycle([image1, image2])

        # return the blinker and image rect
        return blinker, image_rect
