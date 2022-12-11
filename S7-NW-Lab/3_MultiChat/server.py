import socket
from _thread import *

client_names = {}
client_list = []
IP = "127.0.0.1"
PORT = 5000


def send_to_all_clients(from_client, message):
    for to_client in client_list:
        if to_client != from_client:
            try:
                to_client.send(message.encode())
            except:
                to_client.close()
                client_list.remove(to_client)


def handle_client(client, addr):
    name = client_names[addr[0]]
    client.send(f"SERVER >> Welcome, {name}".encode())
    while True:
        try:
            message_enc = client.recv(2048)
            if message_enc:
                message = name + " >> " + str(message_enc.decode())
                print(message)
                send_to_all_clients(client, message)
        except Exception as e:
            print(e)
            continue


def main():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((IP, PORT))
    server.listen(100)
    while True:
        client, addr = server.accept()
        name = client.recv(2048).decode()
        client_names[addr[0]] = name
        client_list.append(client)
        print(f"{name} connected")
        start_new_thread(handle_client, (client, addr))
    server.close()


main()
