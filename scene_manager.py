class SceneManager:
    """Represents an instance of the scene handler."""
    def __init__(self) -> None:
        """Initializes the scene manager object."""
        self.game_screen_active: bool = False
        self.end_screen_active: bool = False
        self.start_screen_active: bool = True

        self.game_paused: bool = False