from src.song import Song
from src.image_processor import ImageProcessor

song_map = [
    ["Unknown", 'bobby_hill.mp3'],
    ["Brandon", "a.mp3"],
    ["Deanna", "crazy_frog.mp3"],
    ["Robin", "the_batman.mp3"],
    ["Log", 'qs.mp3']
]

def choose_song(song: Song, processor: ImageProcessor) -> bool:
    """Chooses the next song that should be played.
    
    Returns `True` if the song is changed and `False` othewise."""

    current_names = processor.current_names.copy()
    previous_names = processor.previous_names.copy()
    people_seen = [*processor.people_seen]
    people_seen_before = [*processor.people_seen_before]
    
    new_people = [name for name in people_seen if name not in people_seen_before]
    people_entering_frame = [name for name in current_names if name not in previous_names]
    people_leaving_frame = [name for name in previous_names if name not in current_names]

    song_matches = [
        pair for pair in song_map 
        if pair[0] in [*new_people, *people_entering_frame, *people_leaving_frame]]

    try:
        song_to_return = f'songs\\{song_matches[0][1]}'
    except:
        song_to_return = 'songs\\sad_trombone.mp3'

    song.change_song(song_to_return)

    return True