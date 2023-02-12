from song import Song
from image_processor import ImageProcessor

song_map: dict[str, str] = {
    "Unknown": 'bobby_hill',
    "Brandon": 'get_money',
    "Deanna": 'crazy_frog',
    "Robin": 'gummy_bear',
    "Log": 'scary_monsters_and_nice_sprites',
    "Pao": 'careless_whisper',
    "Hall": 'hooked_on_a_feeling'
}

def choose_song(song: Song, processor: ImageProcessor) -> bool:
    """Chooses the next song that should be played.
    
    Returns `True` if the song is changed and `False` othewise."""

    current_names = processor.current_names.copy()

    song_matches = [song_map[name] for name in current_names]

    print(f'{song_matches}')

    if len(song_matches) == 0 or song.is_playing():
        return False

    song_to_return = song_matches[0]

    song.change_song(f'songs\\{song_to_return}.mp3')
    
    return True
