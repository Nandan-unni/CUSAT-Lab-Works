import socket

IP = "127.0.0.1"
PORT = 5000
KEY = "1001"


def xor(a, b):
    result = []
    for i in range(1, len(a)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


def mod2div(data):
    cipher_len = len(KEY)
    cipher = data[0:cipher_len]

    while cipher_len < len(data):
        if cipher[0] == "1":
            cipher = xor(cipher, KEY) + data[cipher_len]
        else:
            cipher = xor(cipher, "0" * cipher_len) + data[cipher_len]
        cipher_len += 1

    if cipher[0] == "1":
        cipher = xor(cipher, KEY)
    else:
        cipher = xor(cipher, "0" * cipher_len)

    return cipher


def decrypt(data):

    l_key = len(KEY)
    appended_data = data + "0" * (l_key - 1)
    remainder = mod2div(appended_data)

    return remainder


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    client, addr = server.accept()
    data = client.recv(1024).decode()
    if data:
        print("Recieved: ", data)
        data = decrypt(data)
        print("Remainder:", data)
        check = "0" * (len(KEY) - 1)
        if data == check:
            print("No error found in data")
        else:
            print("Error found in data")
    server.close()


main()
