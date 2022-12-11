import socket

IP = "127.0.0.1"
PORT = 5000


def main():
    client = socket.socket()
    client.connect((IP, PORT))
    while True:
        message = input("CLIENT >> ")
        client.send(message.encode())
        data = client.recv(1024).decode()
        if not data:
            break
        print("SERVER >>", data)
        if data == "bye":
            client.close()
            break


main()
