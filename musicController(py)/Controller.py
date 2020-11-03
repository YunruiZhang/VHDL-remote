import tkinter as tk
from tkinter import *
from tkinter import filedialog
from timer import Timer

import pygame
from PIL import Image, ImageTk

from MusicList import *
from color import *
from socket import *


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

    # socket

    # Define connection (socket) parameters
    # Address + Port no
    # Server would be running on the same host as Client
    # change this port number if required

    serverPort = 12000

    # This line creates the server’s socket. The first parameter indicates the address family; in particular,
    # AF_INET indicates that the underlying network is using IPv4.The second parameter indicates that the socket is
    # of type SOCK_STREAM,which means it is a TCP socket (rather than a UDP socket, where we use SOCK_DGRAM).

    serverSocket = socket(AF_INET, SOCK_STREAM)

    # The above line binds (that is, assigns) the port number 12000 to the server’s socket. In this manner,
    # when anyone sends a packet to port 12000 at the IP address of the server (localhost in this case), that packet
    # will be directed to this socket.

    serverSocket.bind(('localhost', serverPort))

    # The serverSocket then goes in the listen state to listen for client connection requests.

    serverSocket.listen(1)

    print("The server is ready to receive")


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
        inc_vol_btn.place(x=455, y=135)

        dec_vol_img = ImageTk.PhotoImage(Image.open('pics/017-volume down.png').resize((20, 20), Image.ANTIALIAS))
        dec_vol_btn = tk.Button(master=self.window, width=25, height=25, image=dec_vol_img, command=self.dec_vol, bg=WATERMELON)
        dec_vol_btn.place(x=400, y=135)

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

        self.mode_switch_btn.place(x=50, y=250)
        self.mode_switch_btn['command'] = self.mode_sw

        self.set_volume_icon()

        pygame.init()
        pygame.mixer.init()

        self.window.after(1000, self.recvcmd)
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
        self.vol_icon_0.place(x=400-10, y=180) if self.curr_vol.get() > 0 else self.vol_icon_0.place_forget()
        self.vol_icon_1.place(x=410-10, y=180) if self.curr_vol.get() > 1 else self.vol_icon_1.place_forget()
        self.vol_icon_2.place(x=420-10, y=180) if self.curr_vol.get() > 2 else self.vol_icon_2.place_forget()
        self.vol_icon_3.place(x=430-10, y=180) if self.curr_vol.get() > 3 else self.vol_icon_3.place_forget()
        self.vol_icon_4.place(x=440-10, y=180) if self.curr_vol.get() > 4 else self.vol_icon_4.place_forget()
        self.vol_icon_5.place(x=450-10, y=180) if self.curr_vol.get() > 5 else self.vol_icon_5.place_forget()
        self.vol_icon_6.place(x=460-10, y=180) if self.curr_vol.get() > 6 else self.vol_icon_6.place_forget()
        self.vol_icon_7.place(x=470-10, y=180) if self.curr_vol.get() > 7 else self.vol_icon_7.place_forget()
        self.vol_icon_8.place(x=480-10, y=180) if self.curr_vol.get() > 8 else self.vol_icon_8.place_forget()
        self.vol_icon_9.place(x=490-10, y=180) if self.curr_vol.get() > 9 else self.vol_icon_9.place_forget()

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

    def recvcmd(self):
        # give a period to wait
        # t = Timer()
        # t.start()

        # FIXME
        #   Every 2 secs, the python program will send a signal to c++, then c++ send command to python.
        #   This will be done in 100ms.


        # When a client knocks on this door, the program invokes the accept( ) method for serverSocket, which creates
        # a new socket in the server, called connectionSocket, dedicated to this particular client. The client and
        # server then complete the handshaking, creating a TCP connection between the client’s clientSocket and the
        # server’s connectionSocket. With the TCP connection established, the client and server can now send bytes to
        # each other over the connection. With TCP, all bytes sent from one side not are not only guaranteed to
        # arrive at the other side but also guaranteed to arrive in order
        connectionSocket, addr = self.serverSocket.accept()

        # FIXME ^
        #   目前的情况大概是：主UI界面得循环，用mainloop,update,after这些function（否则显示不出来），
        #   然后上面这个accept得等着，如果没接收到东西就会一直卡着。
        #   我的想法是，如果可以，有没有什么办法给上面的动作设定一个期限，超过就跳过。
        #   这是一个多线程的问题。接收信号就不能在UI上操作，反之亦然，就，挺棘手的。
        #   我也在想，希望尽快解决。

        # to indicate ready to receive
        connectionSocket.send(b'Ready')

        # wait for data to arrive from the client
        sentence = connectionSocket.recv(1024)

        # do the corresponding command
        self.do_command(sentence.decode().upper())

        # change the case of the message received from client

        capitalizedSentence = sentence.upper()

        # and send it back to client

        connectionSocket.send(capitalizedSentence)

        # close the connectionSocket. Note that the serverSocket is still alive waiting for new clients to connect,
        # we are only closing the connectionSocket.

        connectionSocket.close()


        self.window.after(1000, self.recvcmd)
