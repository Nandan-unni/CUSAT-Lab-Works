import socket
from string import ascii_lowercase

IP = "127.0.0.1"
PORT = 5000
KEY = 8


def decrypt(message):
    alph = ascii_lowercase
    decipher = ""
    for i in message:
        if i == " ":
            decipher += i
        else:
            decipher += alph[(alph.index(i) - KEY) % 26]
    return decipher


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    client, addr = server.accept()
    data = client.recv(1024).decode()
    if data:
        print("Recieved: ", data)
        data = decrypt(data)
        print("Decrypted:", data)
    server.close()


main()
