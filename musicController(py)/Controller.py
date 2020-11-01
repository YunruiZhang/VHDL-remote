import tkinter as tk
from tkinter import *
from tkinter import filedialog

import pygame

from MusicList import *


class MusicController:

    ml = MusicList()
    directory = ""

    window = tk.Tk()
    curr_dir_label = tk.Label(master=window, width=50, height=2, text="No directory yet...", fg="blue")
    curr_song_label = tk.Label(master=window, width=50, height=2, text="Empty play list...", fg="blue")

    curr_vol = 50
    curr_vol_label = tk.Label(master=window, width=10, height=2, text="Volume: " + str(curr_vol), fg="blue")

    mode_switch_btn = tk.Button(master=window, width=10, height=1, text="Normal", fg="green")

    first_time_play = True

    def __init__(self):
        self.window.geometry("500x300")
        self.window.title("Music Controller")

        play_btn = tk.Button(master=self.window, width=10, height=2, text="PLAY", fg="green", command=self.play)
        play_btn.place(x=0, y=250)

        pause_btn = tk.Button(master=self.window, width=10, height=2, text="PAUSE", fg="green", command=self.pause)
        pause_btn.place(x=100, y=250)

        previous_btn = tk.Button(master=self.window, width=10, height=2, text="PREV", fg="green", command=self.prev)
        previous_btn.place(x=200, y=250)

        next_btn = tk.Button(master=self.window, width=10, height=2, text="NEXT", fg="green", command=self.next)
        next_btn.place(x=300, y=250)

        stop_btn = tk.Button(master=self.window, width=10, height=2, text="STOP", fg="green", command=self.stop)
        stop_btn.place(x=400, y=250)

        quit_btn = tk.Button(master=self.window, width=10, height=2, text="QUIT", fg="red", command=self.quit)
        quit_btn.pack(anchor=NE)

        load_btn = tk.Button(master=self.window, width=10, height=2, text="LOAD", fg="green", command=self.load)
        load_btn.pack(anchor=NE)

        inc_vol_btn = tk.Button(master=self.window, width=10, height=1, text="VOL +", fg="green", command=self.inc_vol)
        inc_vol_btn.place(x=400, y=130)

        dec_vol_btn = tk.Button(master=self.window, width=10, height=1, text="VOL -", fg="green", command=self.dec_vol)
        dec_vol_btn.place(x=400, y=180)

        self.curr_dir_label.place(x=0, y=100)

        self.curr_song_label.place(x=0, y=150)

        self.curr_vol_label.place(x=400, y=150)

        self.mode_switch_btn.place(x=400, y=215)
        self.mode_switch_btn['command'] = self.mode_sw

        pygame.init()
        pygame.mixer.init()

        self.window.mainloop()

    def play(self):
        if self.first_time_play:
            self.first_time_play = False
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def prev(self):
        pygame.mixer.music.load(self.directory + self.ml.choose_next_song(prev=True))
        self.first_time_play = True
        self.curr_song_label['text'] = self.ml.current_song

        # enable auto play
        self.play()

    def next(self):
        pygame.mixer.music.load(self.directory + self.ml.choose_next_song())
        self.first_time_play = True
        self.curr_song_label['text'] = self.ml.current_song

        # enable auto play
        self.play()

    def inc_vol(self):
        self.curr_vol += 5
        self.curr_vol_label['text'] = "Volume: " + str(self.curr_vol)
        pygame.mixer.music.set_volume(self.curr_vol / 100)

    def dec_vol(self):
        self.curr_vol -= 5
        self.curr_vol_label['text'] = "Volume: " + str(self.curr_vol)
        pygame.mixer.music.set_volume(self.curr_vol / 100)

    def quit(self):
        pygame.quit()
        self.window.destroy()

    def load(self):
        # open a directory
        self.directory = filedialog.askdirectory() + "/"
        self.curr_dir_label['text'] = self.directory
        self.ml.load_music_from_directory(directory=self.directory)
        self.curr_song_label['text'] = self.ml.current_song

        # load the first song
        song_full_addr = self.directory + self.ml.current_song
        pygame.mixer.music.load(song_full_addr)
        pygame.mixer.music.set_volume(self.curr_vol / 100)

    def mode_sw(self):
        self.ml.change_play_mode()
        if self.mode_switch_btn['text'] == 'Normal':
            self.mode_switch_btn['text'] = 'Circular'
        elif self.mode_switch_btn['text'] == 'Circular':
            self.mode_switch_btn['text'] = 'Random'
        elif self.mode_switch_btn['text'] == 'Random':
            self.mode_switch_btn['text'] = 'Normal'

    def rec_error_msg(self):
        print('No such Command, please check.')

    def do_command(self, cmd: str):
        sw = {
            'PLAY': self.play,
            'PAUSE': self.pause,
            'STOP': self.stop,
            'PREV': self.prev,
            'NEXT': self.next,
            'VOLUP': self.inc_vol,
            'VOLDN': self.dec_vol,
            'QUIT': self.quit
        }

        sw.get(cmd, self.rec_error_msg)()

