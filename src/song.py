from multiprocessing import Process
from playsound import playsound


class Song:
    """Class for holding a song's name and process."""
    song_name: str
    """Name of the song held by the current process."""
    song_process: Process
    """Subprocess for the current song."""

    def __init__(self, song_name: str) -> None:
        self.song_process = self.new_song(song_name)
        self.song_name = song_name
    #end init
    
    def change_song(self, new_song_name: str) -> None:
        """Changes the current song process to desire.
        
        If a song process is currently running, will attempt to `terminate` and `join` the running process."""
        
        new_song = self.new_song(new_song_name)

        try:
            self.stop()
        except:
            pass
        finally:
            self.song_process = new_song
    #end change_song

    def play(self) -> None:
        """Attempts to start the current song process.
        
        If process is already running, does nothing."""

        try:
            self.song_process.start()
        except:
            return
    #end play

    def stop(self) -> None:
        """Attempts to `terminate` and `join` the current song `Process`.
        
        If `Process` is already terminated or joined, does nothing."""

        try:
            self.song_process.terminate()
            self.song_process.join()
        except:
            return
    #end stop

    def is_playing(self) -> bool:
        """Returns wether or not the process is running"""

        return self.song_process.is_alive()
    #end is_playing


    def new_song(self, song_name: str) -> Process:
        """Returns a new `Process` that will play the desired `.mp3` file."""
        return Process(target=playsound, args=(song_name,), daemon=True)
    #end new_song