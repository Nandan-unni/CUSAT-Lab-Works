import socket

IP = "127.0.0.1"
PORT = 5000


def main():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server.bind((IP, PORT))
    while True:
        data, addr = server.recvfrom(1024)
        if not data:
            break
        data = data.decode()
        print("CLIENT >>", data)
        if data == "bye":
            server.close()
            break
        reply = input("SERVER >> ")
        server.sendto(reply.encode(), addr)
    server.close()


main()
