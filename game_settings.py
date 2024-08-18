class Settings:
    def __init__(self) -> None:
        self.screen_width: int = 300
        self.screen_height: int  = 200

        self.bg_color: tuple[int,int,int] = (240,240,200)
        self.head_color: tuple[int,int,int] = (0,0,0)
        self.body_color: tuple[int,int,int] = (100,100,100)
        self.fruit_color: tuple[int,int,int] = (200,100,100)

        self.snake_size: int = 10
