import socket

IP = "127.0.0.1"
PORT = 5000


def decompresser(compressed):
    compressed = [int(i) for i in compressed.split(";")]
    print("Recieved data :", compressed)
    size = 256
    table = dict((i, chr(i)) for i in range(size))
    processed_msg = table[compressed[0]]
    prev = table[compressed[0]]
    curr = ""
    for num in compressed[1:]:
        if num in table:
            curr = table[num]
        else:
            curr = prev + prev[0]
        processed_msg += curr
        table[size] = prev + curr[0]
        size += 1
        prev = curr
    return processed_msg


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    client, addr = server.accept()
    data = client.recv(1024).decode()
    if data:
        data = decompresser(data)
        print("Decompressed data :", data)
    server.close()


main()
