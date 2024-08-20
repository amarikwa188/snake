from pygame.mixer import Sound


class AudioHandler:
    def __init__(self) -> None:
        self.fruit_sound: Sound = Sound("audio_files/score.mp3")
        self.move_sound: Sound = Sound("audio_files/slither.mp3")
        self.lose_sound: Sound = Sound("audio_files/lose.mp3")
        self.action_sound: Sound = Sound("audio_files/click.mp3")