from pygame.mixer import Sound


class AudioHandler:
    def __init__(self) -> None:
        self.point_sound: Sound = Sound("audio_files/point.mp3")