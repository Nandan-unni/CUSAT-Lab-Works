import socket

IP = "127.0.0.1"
PORT = 5000


def main():
    client = socket.socket()
    client.connect((IP, PORT))
    message = input("CLIENT >> ")
    client.send(message.encode())
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        print("SERVER >>", data)
    client.close()


main()
