import socket

IP = "127.0.0.1"
PORT = 5000


def main():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    while True:
        message = input("CLIENT >> ")
        client.sendto(message.encode(), (IP, PORT))
        data = client.recv(1024).decode()
        if not data:
            break
        print("SERVER >>", data)
        if data == "bye" or message == "bye":
            client.close()
            break


main()
