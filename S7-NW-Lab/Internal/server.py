import socket
import _thread

client_names = {}
client_list = []
IP = "127.0.0.1"
PORT = 8000
no_of_cars = 100


def handle_client(client, addr):
    name = client_names[addr[0]]
    client.send(f"SERVER >> Welcome, {name}".encode())
    while True:
        try:
            message_enc = client.recv(2048)
            if message_enc:
                message = name + " >> " + str(message_enc.decode())
                print(message)
                if "how many cars" in message:
                    reply = str(no_of_cars) + " cars left. Send 'buy' to buy a car."
                    client.send(reply.encode())
                elif "buy" in message:
                    no_of_cars -= no_of_cars
                    reply = name + " bought a car."
                    client.send(reply.encode())
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
        print(name, "connected")
        _thread.start_new_thread(handle_client, (client, addr))
    server.close()


main()
