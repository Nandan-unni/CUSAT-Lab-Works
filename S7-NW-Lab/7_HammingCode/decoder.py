import socket

IP = "127.0.0.1"
PORT = 5000


def no_of_redundant_bits(message):
    m = len(message)
    for r in range(m):
        if 2**r >= m + r + 1:
            return r


def find_error(message, nr):
    n = len(message)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(message[-1 * j])
        res = res + val * (10**i)

    res = str(res)

    return "0" * (4 - len(res)) + res


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    while True:
        client, addr = server.accept()
        message = client.recv(1024).decode()
        if not message:
            break
        rbits = no_of_redundant_bits(message)
        error = find_error(message, rbits)
        check = "0" * rbits
        print("CLIENT >>", message)
        if error == check:
            print("SERVER >> No error in data")
        else:
            error_pos = int(error, 2)
            print("SERVER >> Error found at position", error_pos)
            print("SERVER >> Recieved data: ", message)
            error_pos = len(message) - error_pos
            error_bit = message[error_pos]
            correct_bit = "0" if error_bit == "1" else "1"
            message = message[:error_pos] + correct_bit + message[error_pos + 1 :]
            print("SERVER >> Corrected data:", message)
    server.close()


main()
