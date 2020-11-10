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
    window.geometry("500x300")
    window.title("Music Controller")
    window['bg'] = PRESTIGE_BLUE
    curr_dir_label = tk.Label(master=window, width=50, height=3, text="No directory yet...", fg=TURQUOISE,
                              font='Consolas 10', bg=PRESTIGE_BLUE, anchor='w')
    curr_song_label = tk.Label(master=window, width=50, height=3, text="Empty play list...", fg=TURQUOISE,
                               font='Consolas 9', bg=PRESTIGE_BLUE, anchor='w')

    curr_vol = IntVar()
    curr_vol.set(5)

    first_time_play = True

    normal_play_img = ImageTk.PhotoImage(Image.open('pics/026-repeat.png').resize((20, 20), Image.ANTIALIAS))
    circulate_play_img = ImageTk.PhotoImage(Image.open('pics/028-repeat.png').resize((20, 20)), Image.ANTIALIAS)
    random_play_img = ImageTk.PhotoImage(Image.open('pics/027-shuffle arrows.png').resize((20, 20), Image.ANTIALIAS))

    mode_switch_btn = tk.Button(master=window, width=30, height=30, image=normal_play_img, bg=WISTERIA)

    vol_icon_img = ImageTk.PhotoImage(Image.open('pics/blur.png').resize((5, 5), Image.ANTIALIAS))

    # THE ICON HAVE TO BE SEPARATED
    vol_icon_0 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_1 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_2 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_3 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_4 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_5 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_6 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_7 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_8 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)
    vol_icon_9 = tk.Label(master=window, width=5, height=5, image=vol_icon_img, bg=PRESTIGE_BLUE)

    # irr_img = ImageTk.PhotoImage(Image.open('pics/remote-control.png').resize((30, 30), Image.ANTIALIAS))
    # irr_btn = tk.Button(master=window, width=30, height=30, image=irr_img, bg=NEON_BLUE)

    play_img = ImageTk.PhotoImage(Image.open('pics/020-play.png').resize((20, 20), Image.ANTIALIAS))
    play_btn = tk.Button(master=window, width=30, height=30, image=play_img, bg=EMERALD)
    play_btn.place(x=150, y=250)

    pause_img = ImageTk.PhotoImage(Image.open('pics/021-pause.png').resize((20, 20), Image.ANTIALIAS))
    pause_btn = tk.Button(master=window, width=30, height=30, image=pause_img, bg=SUN_FLOWER)
    pause_btn.place(x=200, y=250)

    prev_img = ImageTk.PhotoImage(Image.open('pics/024-previous.png').resize((20, 20), Image.ANTIALIAS))
    previous_btn = tk.Button(master=window, width=30, height=30, image=prev_img, bg=SATURATED_SKY)
    previous_btn.place(x=100, y=250)

    next_img = ImageTk.PhotoImage(Image.open('pics/023-next.png').resize((20, 20), Image.ANTIALIAS))
    next_btn = tk.Button(master=window, width=30, height=30, image=next_img, bg=SATURATED_SKY)
    next_btn.place(x=300, y=250)

    stop_img = ImageTk.PhotoImage(Image.open('pics/004-disc.png').resize((20, 20), Image.ANTIALIAS))
    stop_btn = tk.Button(master=window, width=30, height=30, image=stop_img, bg=ALIZARIN)
    stop_btn.place(x=250, y=250)

    quit_img = ImageTk.PhotoImage(Image.open('pics/remove.png').resize((20, 20), Image.ANTIALIAS))
    quit_btn = tk.Button(master=window, width=30, height=30, image=quit_img, bg=POMEGRANATE)
    quit_btn.place(x=450, y=0)

    load_img = ImageTk.PhotoImage(Image.open('pics/011-list.png').resize((20, 20), Image.ANTIALIAS))
    load_btn = tk.Button(master=window, width=30, height=30, image=load_img, bg=PUMPKIN)
    load_btn.place(x=450, y=50)

    inc_vol_img = ImageTk.PhotoImage(Image.open('pics/016-volume up.png').resize((20, 20), Image.ANTIALIAS))
    inc_vol_btn = tk.Button(master=window, width=25, height=25, image=inc_vol_img, bg=LIME_SOUP)
    inc_vol_btn.place(x=455, y=135)

    dec_vol_img = ImageTk.PhotoImage(Image.open('pics/017-volume down.png').resize((20, 20), Image.ANTIALIAS))
    dec_vol_btn = tk.Button(master=window, width=25, height=25, image=dec_vol_img, bg=WATERMELON)
    dec_vol_btn.place(x=400, y=135)

    pic1_img = ImageTk.PhotoImage(Image.open('pics/sound.png').resize((80, 80), Image.ANTIALIAS))
    pic1 = tk.Label(master=window, width=80, height=80, image=pic1_img, bg=PRESTIGE_BLUE)
    pic1.place(x=400, y=200)

    dir_img = ImageTk.PhotoImage(Image.open('pics/files.png').resize((30, 30), Image.ANTIALIAS))
    curr_dir_img = tk.Label(master=window, width=40, height=40, image=dir_img, bg=PRESTIGE_BLUE)
    curr_dir_img.place(x=10, y=50)

    song_img = ImageTk.PhotoImage(Image.open('pics/sound-2.png').resize((30, 30), Image.ANTIALIAS))
    curr_song_img = tk.Label(master=window, width=40, height=40, image=song_img, bg=PRESTIGE_BLUE)
    curr_song_img.place(x=10, y=100)

    # self.irr_btn['command'] = self.recvcmd
    # self.irr_btn.place(x=400, y=0)

    curr_dir_label.place(x=60, y=50)

    curr_song_label.place(x=60, y=100)

    mode_switch_btn.place(x=50, y=250)

    pygame.init()
    pygame.mixer.init()

    # self.window.mainloop()

    def __init__(self):
        self.play_btn['command'] = self.play
        self.pause_btn['command'] = self.pause
        self.previous_btn['command'] = self.prev
        self.next_btn['command'] = self.next
        self.stop_btn['command'] = self.stop
        self.load_btn['command'] = self.load
        self.inc_vol_btn['command'] = self.inc_vol
        self.dec_vol_btn['command'] = self.dec_vol
        self.quit_btn['command'] = self.quit
        self.mode_switch_btn['command'] = self.mode_sw

        self.set_volume_icon()

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
        self.first_time_play = True

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
        self.curr_vol.set(min(self.curr_vol.get() + 1, 10))
        pygame.mixer.music.set_volume(self.curr_vol.get() / 10)
        self.set_volume_icon()

    def dec_vol(self):
        self.curr_vol.set(max(self.curr_vol.get() - 1, 0))
        pygame.mixer.music.set_volume(self.curr_vol.get() / 10)
        self.set_volume_icon()

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
        pygame.mixer.music.set_volume(self.curr_vol.get() / 10)

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

    def set_volume_icon(self):
        self.vol_icon_0.place(x=400 - 10, y=180) if self.curr_vol.get() > 0 else self.vol_icon_0.place_forget()
        self.vol_icon_1.place(x=410 - 10, y=180) if self.curr_vol.get() > 1 else self.vol_icon_1.place_forget()
        self.vol_icon_2.place(x=420 - 10, y=180) if self.curr_vol.get() > 2 else self.vol_icon_2.place_forget()
        self.vol_icon_3.place(x=430 - 10, y=180) if self.curr_vol.get() > 3 else self.vol_icon_3.place_forget()
        self.vol_icon_4.place(x=440 - 10, y=180) if self.curr_vol.get() > 4 else self.vol_icon_4.place_forget()
        self.vol_icon_5.place(x=450 - 10, y=180) if self.curr_vol.get() > 5 else self.vol_icon_5.place_forget()
        self.vol_icon_6.place(x=460 - 10, y=180) if self.curr_vol.get() > 6 else self.vol_icon_6.place_forget()
        self.vol_icon_7.place(x=470 - 10, y=180) if self.curr_vol.get() > 7 else self.vol_icon_7.place_forget()
        self.vol_icon_8.place(x=480 - 10, y=180) if self.curr_vol.get() > 8 else self.vol_icon_8.place_forget()
        self.vol_icon_9.place(x=490 - 10, y=180) if self.curr_vol.get() > 9 else self.vol_icon_9.place_forget()

    def do_command(self, cmd: str):
        """
        Do the command
        :param cmd: the text received from socket.
        """
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

    def enable_mainloop(self):
        self.window.mainloop()
