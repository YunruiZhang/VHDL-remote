import tkinter as tk
from tkinter import *
from tkinter import filedialog

import pygame
from PIL import Image, ImageTk

from MusicList import *
from color import *


class MusicController:
    ml = MusicList()
    directory = ""

    window = tk.Tk()
    window['bg'] = PRESTIGE_BLUE
    curr_dir_label = tk.Label(master=window, width=50, height=3, text="No directory yet...", fg=TURQUOISE,
                              font='Consolas 10', bg=PRESTIGE_BLUE, anchor='w')
    curr_song_label = tk.Label(master=window, width=50, height=3, text="Empty play list...", fg=TURQUOISE,
                               font='Consolas 9', bg=PRESTIGE_BLUE, anchor='w')

    curr_vol = IntVar()
    curr_vol.set(50)
    curr_vol_label = tk.Label(master=window, width=4, height=1, textvariable=str(curr_vol), fg=SILVER, bg=PRESTIGE_BLUE)

    first_time_play = True

    normal_play_img = ImageTk.PhotoImage(Image.open('pics/026-repeat.png').resize((20, 20), Image.ANTIALIAS))
    circulate_play_img = ImageTk.PhotoImage(Image.open('pics/028-repeat.png').resize((20, 20)), Image.ANTIALIAS)
    random_play_img = ImageTk.PhotoImage(Image.open('pics/027-shuffle arrows.png').resize((20, 20), Image.ANTIALIAS))

    mode_switch_btn = tk.Button(master=window, width=30, height=30, image=normal_play_img, bg=WISTERIA)

    def __init__(self):
        self.window.geometry("500x300")
        self.window.title("Music Controller")

        play_img = ImageTk.PhotoImage(Image.open('pics/020-play.png').resize((20, 20), Image.ANTIALIAS))
        play_btn = tk.Button(master=self.window, width=30, height=30, image=play_img, command=self.play, bg=EMERALD)
        play_btn.place(x=150, y=250)

        pause_img = ImageTk.PhotoImage(Image.open('pics/021-pause.png').resize((20, 20), Image.ANTIALIAS))
        pause_btn = tk.Button(master=self.window, width=30, height=30, image=pause_img, command=self.pause, bg=SUN_FLOWER)
        pause_btn.place(x=200, y=250)

        prev_img = ImageTk.PhotoImage(Image.open('pics/024-previous.png').resize((20, 20), Image.ANTIALIAS))
        previous_btn = tk.Button(master=self.window, width=30, height=30, image=prev_img, command=self.prev, bg=SATURATED_SKY)
        previous_btn.place(x=100, y=250)

        next_img = ImageTk.PhotoImage(Image.open('pics/023-next.png').resize((20, 20), Image.ANTIALIAS))
        next_btn = tk.Button(master=self.window, width=30, height=30, image=next_img, command=self.next, bg=SATURATED_SKY)
        next_btn.place(x=300, y=250)

        stop_img = ImageTk.PhotoImage(Image.open('pics/004-disc.png').resize((20, 20), Image.ANTIALIAS))
        stop_btn = tk.Button(master=self.window, width=30, height=30, image=stop_img, command=self.stop, bg=ALIZARIN)
        stop_btn.place(x=250, y=250)

        quit_img = ImageTk.PhotoImage(Image.open('pics/remove.png').resize((20, 20), Image.ANTIALIAS))
        quit_btn = tk.Button(master=self.window, width=30, height=30, image=quit_img, command=self.quit, bg=POMEGRANATE)
        quit_btn.place(x=450, y=0)

        load_img = ImageTk.PhotoImage(Image.open('pics/011-list.png').resize((20, 20), Image.ANTIALIAS))
        load_btn = tk.Button(master=self.window, width=30, height=30, image=load_img, command=self.load, bg=PUMPKIN)
        load_btn.place(x=450, y=50)

        inc_vol_img = ImageTk.PhotoImage(Image.open('pics/016-volume up.png').resize((20, 20), Image.ANTIALIAS))
        inc_vol_btn = tk.Button(master=self.window, width=25, height=25, image=inc_vol_img, command=self.inc_vol, bg=LIME_SOUP)
        inc_vol_btn.place(x=455, y=130)

        dec_vol_img = ImageTk.PhotoImage(Image.open('pics/017-volume down.png').resize((20, 20), Image.ANTIALIAS))
        dec_vol_btn = tk.Button(master=self.window, width=25, height=25, image=dec_vol_img, command=self.dec_vol, bg=WATERMELON)
        dec_vol_btn.place(x=400, y=130)

        pic1_img = ImageTk.PhotoImage(Image.open('pics/sound.png').resize((80, 80), Image.ANTIALIAS))
        pic1 = tk.Label(master=self.window, width=80, height=80, image=pic1_img, bg=PRESTIGE_BLUE)
        pic1.place(x=400, y=200)

        dir_img = ImageTk.PhotoImage(Image.open('pics/files.png').resize((30, 30), Image.ANTIALIAS))
        curr_dir_img = tk.Label(master=self.window, width=40, height=40, image=dir_img, bg=PRESTIGE_BLUE)
        curr_dir_img.place(x=10, y=50)

        song_img = ImageTk.PhotoImage(Image.open('pics/sound-2.png').resize((30, 30), Image.ANTIALIAS))
        curr_song_img = tk.Label(master=self.window, width=40, height=40, image=song_img, bg=PRESTIGE_BLUE)
        curr_song_img.place(x=10, y=100)

        self.curr_dir_label.place(x=60, y=50)

        self.curr_song_label.place(x=60, y=100)

        self.curr_vol_label.place(x=455, y=180)

        self.mode_switch_btn.place(x=50, y=250)
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
        self.curr_vol.set(min(self.curr_vol.get() + 10, 100))
        pygame.mixer.music.set_volume(self.curr_vol.get() / 100)

    def dec_vol(self):
        self.curr_vol.set(max(self.curr_vol.get() - 10, 0))
        pygame.mixer.music.set_volume(self.curr_vol.get() / 100)

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
        pygame.mixer.music.set_volume(self.curr_vol.get() / 100)

    def mode_sw(self):
        self.ml.change_play_mode()
        self.set_order_icon()

    def rec_error_msg(self):
        print('No such command, please check.')

    def set_order_icon(self):
        if self.ml.play_mode == normal_play:
            self.mode_switch_btn['image'] = self.normal_play_img
        elif self.ml.play_mode == random_play:
            self.mode_switch_btn['image'] = self.random_play_img
        elif self.ml.play_mode == circulate_play:
            self.mode_switch_btn['image'] = self.circulate_play_img

    def do_command(self, cmd: str):
        '''
        Do the command
        :param cmd: the text received from socket.
        '''
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
