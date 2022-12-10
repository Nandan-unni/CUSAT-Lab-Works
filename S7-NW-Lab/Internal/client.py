import socket
import sys, select, socket
from _thread import *


IP = "127.0.0.1"
PORT = 8000


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP, PORT))
    name = input("Enter your name >> ")
    server.send(name.encode())

    while True:
        sockets_list = [sys.stdin, server]
        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
        for socks in read_sockets:
            if socks == server:
                message_enc = socks.recv(2048)
                if message_enc:
                    print(message_enc.decode())
            else:
                message = sys.stdin.readline()
                server.send(message.encode())
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()


main()
