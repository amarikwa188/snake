class SceneManager:
    def __init__(self) -> None:
        self.game_screen_active: bool = False
        self.end_screen_active: bool = False
        self.start_screen_active: bool = True

        self.game_paused: bool = False