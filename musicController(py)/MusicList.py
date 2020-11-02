import random
from os import listdir

# Music Play Mode
circulate_play = 0
random_play = 1
normal_play = 2


class MusicList:
    music_list = list()
    play_mode = normal_play
    current_song = None

    def __init__(self):
        pass

    def music_amount(self):
        return len(self.music_list)

    def load_music_from_directory(self, directory: str, append=False):
        audio_format = ('.mp3', '.wav', '.wma', '.m4a', '.aac')
        music_list_in_dir = [f for f in listdir(directory) if (f.lower().endswith(audio_format))]
        if append:
            self.music_list.extend(music_list_in_dir)
        else:
            self.music_list = music_list_in_dir

        if len(music_list_in_dir) > 0:
            print("%d success, %d fail, %d total." %
                  (len(music_list_in_dir), len(listdir(directory)) - len(music_list_in_dir), self.music_amount()))
            self.current_song = self.music_list[0]
        else:
            raise ImportError("0 songs found or import fail.")

    def remove_item(self, *item: str):
        self.music_list = [m for m in self.music_list if m not in item]

    def get_current_song(self) -> str:
        return self.current_song

    def get_current_song_index(self) -> int:
        return self.music_list.index(self.current_song)

    def choose_next_song(self, prev=False) -> str:
        i = self.get_current_song_index()
        if self.play_mode == normal_play:
            if prev:
                i = i - 1 if i - 1 >= 0 else self.music_amount() - 1
            else:
                i = (self.get_current_song_index() + 1) % self.music_amount()

        elif self.play_mode == random_play:
            j = i
            while(j == i):
                j = random.randint(0, len(self.music_list))
            i = j

        self.current_song = self.music_list[i]
        return self.get_current_song()

    def choose_next_song_index(self) -> int:
        return self.music_list.index(self.choose_next_song)

    def change_play_mode(self):
        self.play_mode = (self.play_mode + 1) % 3
