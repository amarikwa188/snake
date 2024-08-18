class Settings:
    def __init__(self) -> None:
        self.screen_width: int = 500
        self.screen_height: int  = 400

        self.bg_color: tuple[int,int,int] = (240,240,200)
        self.head_color: tuple[int,int,int] = (0,0,0)
        self.body_color: tuple[int,int,int] = (100,100,100)

        self.snake_size: int = 10
