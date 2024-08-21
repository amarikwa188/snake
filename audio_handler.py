from pygame import mixer
from pygame.mixer import Sound


class AudioHandler:
    def __init__(self) -> None:
        # background music
        mixer.init()
        mixer.music.load("audio_files/background.mp3")
        mixer.music.set_volume(0.05)
        mixer.music.play(-1)


        # sound effects
        self.fruit_sound: Sound = Sound("audio_files/score.mp3")
        self.move_sound: Sound = Sound("audio_files/slither.mp3")
        self.lose_sound: Sound = Sound("audio_files/lose.mp3")
        self.action_sound: Sound = Sound("audio_files/click.mp3")