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
            # filling reduntant bit pos with "x"
            new_msg = new_msg + "x"
            pos_pow += 1
        else:
            new_msg = new_msg + msg[-1 * pos_from_last]
            pos_from_last += 1

    return new_msg[::-1]


def val_of_redundant_bits(message, rbits):
    msg_len = len(message)
    for i in range(rbits):
        red_pos = 2**i
        # red_pos will be 1, 2, 4, 8
        # message[red_pos] conatins "x"
        total_1 = 0
        parity_val = "1"
        for j in range(msg_len):
            j_bin = num_to_bin(j, rbits)
            # arr[-3] means 3rd bit from last
            # eg: arr = "1011", arr[-3] is 0
            if j_bin[-1 * (i + 1)] == "1":
                if message[j] == "1":
                    total_1 += 1
        if total_1 % 2 == 0:
            parity_val = "0"
        # replacing x with parity_val
        message = replace_from_last(message, red_pos, parity_val)
    return message


def main():
    message = "1011001"
    rbits = no_of_redundant_bits(message)
    message = pos_of_redundant_bits(message, rbits)
    enc_msg = val_of_redundant_bits(message, rbits)
    print(enc_msg, len(enc_msg))


main()
