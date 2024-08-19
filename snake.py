import random as rng

import pygame
from pygame import Surface, Rect

from game_settings import Settings
from ui_handler import UIHandler
from scene_manager import SceneManager

import shelve


class Node:
    """Represents a single section of the snake's body."""
    def __init__(self, settings: Settings) -> None:
        """
        Initializes a node.

        :param settings: a reference to the game settings.
        """
        self.x_pos: int = settings.screen_width // 2
        self.y_pos: int = settings.screen_height // 2

        self.next: Node | None = None


class Snake:
    """A linked list representing the snake."""
    def __init__(self, settings: Settings, screen: Surface,
                 ui: UIHandler, scene: SceneManager) -> None:
        """
        Initializes a snake object.

        :param settings: the game settings.
        :param screen: a reference to the screen.
        :param ui: a reference to the ui handler.
        :param scene: the scene manager.
        """
        # set up references to the settings, screen, ui and scene managers
        self.settings: Settings = settings
        self.screen: Surface = screen
        self.ui: UIHandler = ui
        self.scene: SceneManager = scene

        # set size of a the snake's parts
        self.size: int =  self.settings.snake_size

        # set the length that the snake should be as well as the current
        # number of nodes
        self.length: int = 1
        self.current_length: int = 1

        # set the speed of the snake
        self.speed_x, self.speed_y = 0, 0

        # create a head node
        self.head: Node = Node(self.settings)

        # spawn a fruit
        self.fruit: tuple[int,int] = (0,0)
        self.spawn_fruit()

        # load highscore
        self.highscore = 0
        self.data: shelve.Shelf = shelve.open("save_data/hs.txt")
        try:
            self.highscore: int = self.data["hs"]
        except KeyError:
            self.data["hs"] = self.highscore
        self.data.close()


    def update(self) -> None:
        """
        Update the position of the snake.
        """
        # get new position
        new_x = self.head.x_pos + self.speed_x
        new_y = self.head.y_pos + self.speed_y

        # add new head
        new_head: Node = Node(self.settings)

        new_head.x_pos = new_x
        new_head.y_pos = new_y

        new_head.next = self.head
        self.head = new_head

        # delete the tail or add
        if self.length == self.current_length:
            current_node: Node = self.head
            while current_node.next and current_node.next.next:
                current_node = current_node.next

            current_node.next = None
        else:
            self.current_length += 1

        # check for fruit
        if (new_x, new_y) == self.fruit:
            self.length += 1
            self.ui.score += 1
            self.spawn_fruit()

        # check for collision with tail
        if not self.head.next:
            return
        
        current_node: Node | None = self.head.next
        while current_node:
            if (new_x,new_y) == (current_node.x_pos,current_node.y_pos):
                self.end_game()
                return
            current_node = current_node.next
            

    def draw_snake(self) -> None:
        """
        Draw the each node of the snake in the appropriate positions.
        """
        # draw fruit
        fruit_rect: Rect = Rect(0,0, self.size, self.size)
        fruit_rect.x, fruit_rect.y = self.fruit[0], self.fruit[1]
        pygame.draw.rect(self.screen, self.settings.fruit_color, fruit_rect)

        # draw snake
        current_node: Node = self.head

        while current_node:
            rect: Rect = Rect(0,0, self.size, self.size)
            rect.x = current_node.x_pos
            rect.y = current_node.y_pos

            color: tuple[int,int,int] = self.settings.head_color if \
                                        current_node == self.head else \
                                        self.settings.body_color

            pygame.draw.rect(self.screen, color, rect)

            # check if out of bounds
            if current_node == self.head:
                out_of_bounds: bool = rect.left < 0 or \
                      rect.right > self.settings.screen_width or \
                      rect.top < 0 or \
                      rect.bottom > self.settings.screen_height
                if out_of_bounds:
                    self.end_game()
                
            current_node = current_node.next


    def spawn_fruit(self) -> None:
        """
        Spawn a fruit in a random position.
        """
        # ensure the fruit is in a new position and not on the
        # snake's tail
        current_pos: tuple[int,int] = self.fruit
        new_x: int = rng.randint(1,28) * 10
        new_y: int = rng.randint(1,18) * 10
        new_pos: tuple[int,int] = (new_x, new_y)

        current_node: Node | None = self.head
        positions: list[tuple[int,int]] = []
        while current_node:
            positions.append((current_node.x_pos, current_node.y_pos))
            current_node = current_node.next

        while current_pos == new_pos or new_pos in positions:
            new_x = rng.randint(1,28) * 10
            new_y = rng.randint(1,18) * 10
            new_pos = (new_x, new_y)

        # set fruit position
        self.fruit = (new_x, new_y)

    
    def end_game(self) -> None:
        self.scene.game_screen_active = False
        self.scene.end_screen_active = True
        pygame.time.set_timer(self.ui.BLINKEVENT, 500)

        if self.ui.score > self.highscore:
            self.highscore = self.ui.score

        self.data: shelve.Shelf = shelve.open("save_data/hs.txt")
        self.data["hs"] = self.highscore
        self.data.close() 

        print(self.highscore)


    def reset_snake(self) -> None:
        """
        Reset the snake at the start of a new game.
        """
        # delete all tail nodes
        self.head.next = None

        # reset the position
        self.head.x_pos = self.settings.screen_width // 2
        self.head.y_pos = self.settings.screen_height // 2

        # reset the length and speed attributes
        self.length: int = 1
        self.current_length: int = 1
        self.speed_x, self.speed_y = 0, 0