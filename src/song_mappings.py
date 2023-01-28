from song import Song
from image_processor import ImageProcessor
from typing import Callable

class Sound():
    song: Callable[..., str]
    priority: int
    def __init__(self, song: str, prio: int) -> None:
        self.song = song
        self.priority = prio

song_map: dict[str, Sound] = {
    "Unknown": Sound(lambda x: 'bobby_hill.mp3', 10),
    "Brandon": Sound(lambda x: 'barcelona.mp3' if 'Deanna' in x else 'a.mp3', 1),
    "Deanna": Sound(lambda x: 'crazy_frog.mp3', 2),
    "Robin": Sound(lambda x: 'the_batman.mp3', 4),
    "Log": Sound(lambda x: 'qs.mp3', 4),
    "Pao" : Sound(lambda x: ('boom_boom_pao.mp3', 'careless_whisper.mp3', 'barbie_girl.mp3')[len(x) - 1 if len(x) < 3 else 2], 0),
}

def choose_song(song: Song, processor: ImageProcessor) -> bool:
    """Chooses the next song that should be played.
    
    Returns `True` if the song is changed and `False` othewise."""

    current_names = processor.current_names.copy()
    previous_names = processor.previous_names.copy()
    people_seen = [*processor.people_seen.copy()]
    people_seen_before = [*processor.people_seen_before.copy()]
    
    new_people = [name for name in people_seen if name not in people_seen_before]
    people_entering_frame = [name for name in current_names if name not in previous_names]
    people_leaving_frame = [name for name in previous_names if name not in current_names]

    # song_matches = [song_map[name] for name in {*new_people, *people_entering_frame, *people_leaving_frame}]
    song_matches = [song_map[name] for name in current_names]

    song_matches = sorted(song_matches, key=lambda x: x.priority, reverse=False) 
    if len(song_matches) == 0:
        return False

    sound_from_matches = song_matches[0]
    sound_to_return = sound_from_matches.song(current_names) if callable(sound_from_matches.song) else sound_from_matches.song
    sound_to_return = f'songs\\{sound_to_return}'

    print(f'[NOTICE] Playing {sound_to_return}.')
    song.change_song(sound_to_return)
    
    return True