from socket import *

from Controller import *

import threading

# socket

serverPort = 12002

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', serverPort))

serverSocket.listen(1)

print("The server is ready to receive.")


def sk(mc: MusicController):
    # while 1:
    #     connection_socket, addr = serverSocket.accept()
    #
    #     sentence = connection_socket.recv(1024)
    #
    #     mc.do_command(sentence.decode().upper())
    #
    #     capitalized_sentence = sentence.upper()
    #
    #     connection_socket.send(capitalized_sentence)
    #
    #     connection_socket.close()

    for i in range(10):
        print(i)


if __name__ == '__main__':
    m = MusicController()
    thr = threading.Thread(target=sk, args=[m, ])
    thr.start()
    m.enable_mainloop()
