import socket

IP = "127.0.0.1"
PORT = 5000


def num_to_bin(num, max_len):
    bin_val = bin(num).replace("0b", "")
    # 10 to 0010
    bin_val = "0" * (max_len - len(bin_val)) + bin_val
    return bin_val


def replace_from_last(parent_str, pos, child_str):
    parent_str = parent_str[::-1]
    parent_str = parent_str[: pos - 1] + child_str + parent_str[pos:]
    return parent_str[::-1]


def no_of_redundant_bits(message):
    m = len(message)
    for r in range(m):
        if 2**r >= m + r + 1:
            return r


def pos_of_redundant_bits(msg, rbits):
    pos_pow = 0
    pos_from_last = 1
    m = len(msg)
    new_msg = ""

    for i in range(1, m + rbits + 1):
        if i == 2**pos_pow:
            # filling reduntant bit pos with "0"
            new_msg = new_msg + "0"
            pos_pow += 1
        else:
            new_msg = new_msg + msg[-1 * pos_from_last]
            pos_from_last += 1

    return new_msg[::-1]


def val_of_redundant_bits(message, rbits):
    m = len(message)

    for i in range(rbits):
        val = 0
        for j in range(1, m + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(message[-1 * j])

        message = message[: m - (2**i)] + str(val) + message[m - (2**i) + 1 :]
    return message


def main():
    client = socket.socket()
    client.connect((IP, PORT))
    message = input("CLIENT >> ")
    rbits = no_of_redundant_bits(message)
    message = pos_of_redundant_bits(message, rbits)
    emessage = val_of_redundant_bits(message, rbits)
    client.send(emessage.encode())
    client.close()


main()
