import socket

IP = "127.0.0.1"
PORT = 5000


def decompresser(compressed):
    compressed = [int(i) for i in compressed.split(";")]
    print("Recieved data :", compressed)
    size = 256
    processed_msg = ""
    table = dict((i, chr(i)) for i in range(size))
    prev = ""
    for num in compressed:
        processed_msg += table[num]
        if not prev == "":
            table[size] = prev + table[num][0]
            size += 1
        prev = table[num]
    return processed_msg


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    while True:
        client, addr = server.accept()
        data = client.recv(1024).decode()
        if not data:
            break
        data = decompresser(data)
        print("Decompressed data :", data)
    server.close()


main()
