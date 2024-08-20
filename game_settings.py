class Settings:
    """Represents an instance of the game settings."""
    def __init__(self) -> None:
        """Initializes an instance of the settings class."""
        # screen dimensions
        self.screen_width: int = 300
        self.screen_height: int  = 200

        # game colors
        self.bg_color: tuple[int,int,int] = (240,240,200)
        self.head_color: tuple[int,int,int] = (50,100,50)
        self.body_color: tuple[int,int,int] = (50,200,100)
        self.fruit_color: tuple[int,int,int] = (200,100,100)
        self.score_color: tuple[int,int,int] = (200,200,160)

        # snake dimensions
        self.snake_size: int = 10
