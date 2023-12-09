import sys
from b64alphabet import get_alphabet

alphabet = get_alphabet()

def get_key(dic, value):
    for key, val in dic.items():
        if value == val:
            return key

    return None

def get_bin_string(source):
    bin_string = ""
    for c in source:
        if c != '=':
            bin_string += get_key(alphabet, c)

    return bin_string

def decode(source):
    bin_string = get_bin_string(source)
    len_str = len(bin_string)
    decoded = ""

    for i in range(0, len_str, 8):
        chunk = bin_string[i:i+8]
        decimal = int(chunk, 2)    # binary to decimal
        decoded += chr(decimal)

    return decoded

def main():
    if len(sys.argv) < 2:
        print("argument required: message to decode")
        exit(1)

    source = sys.argv[1]
    decoded = decode(source)

    print(decoded)

if __name__ == '__main__':
    main()
