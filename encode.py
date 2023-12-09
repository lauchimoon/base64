import sys
from b64alphabet import get_alphabet

def get_bin_string(source_string):
    bin_string = ""

    for c in source_string:
        ascii_value = ord(c)
        binary_value = bin(ascii_value)[2:].zfill(8)
        bin_string += binary_value

    return bin_string

def get_6bit_chunks(bin_string):
    chunks = []
    len_str = len(bin_string)

    for i in range(0, len_str, 6):
        chunks.append(bin_string[i:i+6])

    # If a chunk doesn't have 6 bits, add as many ceroes as necessary
    for ch in enumerate(chunks):
        idx = ch[0]
        len_ch = len(ch[1])
        if len_ch != 6:
            missing_zeros = 6 - len_ch
            chunks[idx] += '0'*missing_zeros

    # If the string's length is not a multiple of twenty-four, add padding
    len_chunks = len(chunks)
    if len_str % 24 != 0:
        missing_paddings = 4 - len_chunks % 4
        for _ in range(missing_paddings):
            chunks.append('0')

    return chunks

def encode(source):
    alphabet = get_alphabet()
    bin_string = get_bin_string(source)
    chunks = get_6bit_chunks(bin_string)

    encoded = ""
    for chunk in chunks:
        encoded += alphabet[chunk]

    return encoded

def main():
    if len(sys.argv) < 2:
        print("argument required: message to encode")
        exit(1)

    source = sys.argv[1]
    encoded = encode(source)
    print(encoded)

if __name__ == '__main__':
    main()

