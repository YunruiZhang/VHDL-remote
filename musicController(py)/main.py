from Controller import *
from socket import *


if __name__ == '__main__':

    m = MusicController()
    # socket

    # Define connection (socket) parameters
    # Address + Port no
    # Server would be running on the same host as Client
    # change this port number if required

    # serverPort = 12000

    # This line creates the server’s socket. The first parameter indicates the address family; in particular,
    # AF_INET indicates that the underlying network is using IPv4.The second parameter indicates that the socket is
    # of type SOCK_STREAM,which means it is a TCP socket (rather than a UDP socket, where we use SOCK_DGRAM).

    # serverSocket = socket(AF_INET, SOCK_STREAM)

    # The above line binds (that is, assigns) the port number 12000 to the server’s socket. In this manner,
    # when anyone sends a packet to port 12000 at the IP address of the server (localhost in this case), that packet
    # will be directed to this socket.

    # serverSocket.bind(('localhost', serverPort))

    # The serverSocket then goes in the listen state to listen for client connection requests.

    # serverSocket.listen(1)

    # print("The server is ready to receive")

    # while 1:
        # When a client knocks on this door, the program invokes the accept( ) method for serverSocket, which creates
        # a new socket in the server, called connectionSocket, dedicated to this particular client. The client and
        # server then complete the handshaking, creating a TCP connection between the client’s clientSocket and the
        # server’s connectionSocket. With the TCP connection established, the client and server can now send bytes to
        # each other over the connection. With TCP, all bytes sent from one side not are not only guaranteed to
        # arrive at the other side but also guaranteed to arrive in order
        # connectionSocket, addr = serverSocket.accept()

        # wait for data to arrive from the client

        # sentence = connectionSocket.recv(1024)

        # m.do_command(sentence.decode().upper())

        # change the case of the message received from client

        # capitalizedSentence = sentence.upper()

        # and send it back to client

        # connectionSocket.send(capitalizedSentence)

        # close the connectionSocket. Note that the serverSocket is still alive waiting for new clients to connect,
        # we are only closing the connectionSocket.

        # connectionSocket.close()
