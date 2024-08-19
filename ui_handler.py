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
        ## game fonts
        self.score_font_single: Font = pygame.font.\
            SysFont(None, 300)
        self.score_font_double: Font = pygame.font.\
             SysFont(None, 260)
        self.instructions_font: Font = pygame.font.\
            SysFont(None, 50)
        self.score_color: tuple[int,int,int] = self.settings.score_color

        # menu fonts
        menu_font = "Trebuchet MS"
        self.game_over_font: Font = pygame.font.SysFont(menu_font, 45)
        self.final_score_font: Font = pygame.font.SysFont(menu_font, 18)
        self.blinker_font: Font = pygame.font.SysFont(menu_font, 15)
        self.pause_font: Font = pygame.font.SysFont(menu_font, 50)
        self.title_font: Font = pygame.font.SysFont(menu_font, 60)
        self.button_font: Font = pygame.font.SysFont(menu_font, 16)

        # keep track of the score and whether the snake has started movings
        self.score: int = 0
        self.highscore: int  = 0
        self.moving: bool = False

        # handle blinking text
        self.BLINKEVENT: int = pygame.USEREVENT + 1

        play_text: str = "Press P to play again..."
        self.play_blinker, self.play_rect = self.blinker(play_text)
        self.play_current: Surface = next(self.play_blinker)

        # for start screen animation
        self.menu_fruit: tuple[int,int] = (self.settings.screen_width//2,
                                           self.settings.screen_height//2)
        self.menu_head: tuple[int,int] = (self.settings.screen_width//2 - 60,
                                          self.settings.screen_height//2)
        self.menu_part1: tuple[int,int] = (self.settings.screen_width//2 - 70,
                                          self.settings.screen_height//2)
        self.menu_part2: tuple[int,int] = (self.settings.screen_width//2 - 80,
                                          self.settings.screen_height//2)
        
        # start screen button
        self.start_hover: bool = False


    def draw_ui(self) -> None:
        """
        Draw the ui to the screen.
        """
        # start screen
        if self.scene.start_screen_active:
            self.start_screen_animation()
            self.start_screen_title()
            self.start_button()

        # game screen
        if self.scene.game_screen_active:
            self.game_display()
            
        # end screen
        if self.scene.end_screen_active:
            self.display_game_over()
            self.screen.blit(self.play_current, self.play_rect)


    def start_screen_animation(self) -> None:
        size: int = self.settings.snake_size
        fruit_y: int = self.menu_fruit[1] % self.settings.screen_height
        head_y: int = self.menu_head[1] % self.settings.screen_height
        part1_y: int = self.menu_part1[1] % self.settings.screen_height
        part2_y: int = self.menu_part2[1] % self.settings.screen_height

        # fruit animation
        new_x: int = (self.menu_fruit[0] + 10)
        if new_x == self.settings.screen_width:
            fruit_y += 10
        new_x = new_x % self.settings.screen_width
        self.menu_fruit = (new_x, fruit_y)
        fruit_rect: Rect = Rect(0,0,size,size)
        fruit_rect.x = new_x
        fruit_rect.y = fruit_y
        pygame.draw.rect(self.screen, self.settings.fruit_color,fruit_rect)
        
        # snake animation
        ## head
        new_x = (self.menu_head[0] + 10) 
        if new_x == self.settings.screen_width:
            head_y += 10
        new_x = new_x % self.settings.screen_width
        self.menu_head = (new_x, head_y)
        head_rect: Rect = Rect(0,0,size,size)
        head_rect.x = new_x
        head_rect.y = head_y
        pygame.draw.rect(self.screen, self.settings.head_color, head_rect)

        ## part 1
        new_x = (self.menu_part1[0] + 10) 
        if new_x == self.settings.screen_width:
            part1_y += 10
        new_x = new_x % self.settings.screen_width
        self.menu_part1 = (new_x, part1_y)
        part1_rect: Rect = Rect(0,0,size,size)
        part1_rect.x = new_x
        part1_rect.y = part1_y
        pygame.draw.rect(self.screen, self.settings.body_color,part1_rect)

        ## part 2
        new_x = (self.menu_part2[0] + 10) 
        if new_x == self.settings.screen_width:
            part2_y += 10
        new_x = new_x % self.settings.screen_width
        self.menu_part2 = (new_x, part2_y)
        part2_rect: Rect = Rect(0,0,size,size)
        part2_rect.x = new_x
        part2_rect.y = part2_y
        pygame.draw.rect(self.screen, self.settings.body_color,part2_rect)


    def start_screen_title(self) -> None:
        text: str = "SNAKE"
        image: Surface = self.title_font.render(text, True, (0,0,0))
        image_rect: Rect = image.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = self.screen_rect.centery - 20
        self.screen.blit(image, image_rect)


    def start_button(self) -> None:
        button: Rect = Rect(0,0, 60,25)
        button.centerx = self.screen_rect.centerx
        button.centery = self.screen_rect.centery + 40

        text: str = 'PLAY'
        message: Surface = self.button_font.render(text, True, (255,255,255))
        message_rect: Rect = message.get_rect()
        message_rect.center = button.center

        button_color: tuple[int,int,int] = (0,0,0)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.start_hover = False

        if button.left < mouse_x < button.right and \
            button.top < mouse_y < button.bottom:
            button_color = (100,100,100)
            self.start_hover = True

        self.screen.fill(button_color, button)
        self.screen.blit(message, message_rect)


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


    def display_pause(self) -> None:
        text: str = "PAUSED"
        image: Surface = self.pause_font.render(text, True, (0,0,0))
        image_rect: Rect = image.get_rect()
        image_rect.center = self.screen_rect.center
        self.screen.blit(image, image_rect)


    def display_game_over(self) -> None:
        """
        Display a game over message and the final score on the end screen.
        """
        text: str = "GAME OVER"
        image: Surface = self.game_over_font.render(text, True, (200,0,0))
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
