import socket

IP = "127.0.0.1"
PORT = 5000


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    while True:
        client, addr = server.accept()
        data = client.recv(1024).decode()
        if not data:
            break
        print("CLIENT >>", data)
        reply = input("SERVER >> ")
        client.send(reply.encode())
    server.close()


main()
