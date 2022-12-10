import socket
from string import ascii_lowercase

IP = "127.0.0.1"
PORT = 5000
KEY = 8


def encrypt(message):
    alph = ascii_lowercase
    cipher = ""
    for i in message:
        if i == " ":
            cipher += i
        else:
            cipher += alph[(alph.index(i) + KEY) % 26]
    return cipher


def main():
    client = socket.socket()
    client.connect((IP, PORT))
    message = input("Enter message: ")
    message = encrypt(message.lower())
    print("Encrypted message: ", message)
    client.send(message.encode())
    client.close()


main()
