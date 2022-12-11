import socket

IP = "127.0.0.1"
PORT = 5000


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    client, addr = server.accept()
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        print("CLIENT >>", data)
        if data == "bye":
            client.close()
            break
        reply = input("SERVER >> ")
        client.send(reply.encode())
    server.close()


main()
