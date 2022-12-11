import socket
import math

IP = "127.0.0.1"
PORT = 5000
KEY = "hack"


def decrypt(message):
    no_of_col = len(KEY)
    no_of_row = int(math.ceil(len(message) / no_of_col))

    msg_id = 0
    key_id = 0

    key_list = sorted(list(KEY))
    msg_list = list(message)

    decipher = []

    for _ in range(no_of_row):
        decipher += [[None] * no_of_col]

    for _ in range(no_of_col):
        curr_id = KEY.index(key_list[key_id])
        for j in range(no_of_row):
            decipher[j][curr_id] = msg_list[msg_id]
            msg_id += 1
        key_id += 1

    msg = ""
    for i in range(no_of_row):
        for j in range(no_of_col):
            msg += decipher[i][j]

    no_of_null = msg.count("_")

    if no_of_null > 0:
        return msg[:-no_of_null]

    return msg


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    client, addr = server.accept()
    data = client.recv(1024).decode()
    if not data:
        print("Recieved: ", data)
        data = decrypt(data)
        print("Decrypted:", data)
    server.close()


main()
