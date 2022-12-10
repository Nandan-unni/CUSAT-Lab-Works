import socket
import math

IP = "127.0.0.1"
PORT = 5000
KEY = "HACK"


def encrypt(message):
    no_of_col = len(KEY)
    no_of_row = int(math.ceil(len(message) / no_of_col))

    msg_len = float(len(message))

    cipher = ""
    key_id = 0
    key_list = sorted(list(KEY))
    msg_list = list(message)

    no_of_null = int((no_of_row * no_of_col) - msg_len)
    msg_list.extend("_" * no_of_null)
    matrix = [msg_list[i : i + no_of_col] for i in range(0, len(msg_list), no_of_col)]

    for _ in range(no_of_col):
        curr_id = KEY.index(key_list[key_id])
        cipher += "".join([row[curr_id] for row in matrix])
        key_id += 1

    return cipher


def main():
    client = socket.socket()
    client.connect((IP, PORT))
    message = input("Enter message: ")
    message = encrypt(message)
    print("Encrypted message: ", message)
    client.send(message.encode())
    client.close()


main()
