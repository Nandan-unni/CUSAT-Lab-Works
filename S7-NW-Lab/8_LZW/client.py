import socket

IP = "127.0.0.1"
PORT = 5000


def compresser(message):
    size = 256
    compressed = []
    table = dict((chr(i), i) for i in range(size))
    curr = ""
    for ch in message:
        curr += ch
        if not curr in table:
            table[curr] = size
            size += 1
            compressed.append(table[curr[:-1]])
            curr = ch
    compressed.append(table[curr])
    print("Compressed message :", compressed)
    return ";".join([str(i) for i in compressed])


def main():
    client = socket.socket()
    client.connect((IP, PORT))
    message = input("Enter message: ")
    message = compresser(message)
    client.send(message.encode())
    client.close()


main()
