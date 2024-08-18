import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite

from game_settings import Settings


class Snake:
    def __init__(self) -> None:
        self.head: Body | None = None


class Body:
    def __init__(self) -> None:
        self.x_pos: int = 0
        self.y_pos: int = 0

        self.next: Body | None = None
