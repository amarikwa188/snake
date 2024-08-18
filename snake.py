import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite

from game_settings import Settings


class Snake:
    def __init__(self, settings: Settings, screen: Surface) -> None:
        self.settings: Settings = settings
        self.screen: Surface = screen

        self.size: int =  self.settings.snake_size
        self.speed_x, self.speed_y = 0, 0

        self.head: Node = Node(self.settings)

    def update(self) -> None:
        # add new head
        new_head: Node = Node(self.settings)
        new_x = self.head.x_pos + self.speed_x
        new_y = self.head.y_pos + self.speed_y

        new_head.x_pos = new_x
        new_head.y_pos = new_y

        new_head.next = self.head
        self.head = new_head

        # delete the tail
        current_node: Node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def draw_snake(self) -> None:
        current_node: Node = self.head

        while current_node:
            rect: Rect = Rect(0,0, self.size, self.size)
            rect.centerx = current_node.x_pos
            rect.centery = current_node.y_pos

            color: tuple[int,int,int] = self.settings.head_color if \
                                        current_node == self.head else \
                                        self.settings.body_color

            pygame.draw.rect(self.screen, color, rect)
            current_node = current_node.next


class Node:
    def __init__(self, settings: Settings) -> None:
        self.x_pos: int = settings.screen_width // 2
        self.y_pos: int = settings.screen_height // 2

        self.next: Node | None = None
