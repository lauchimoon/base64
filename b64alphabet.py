def get_alphabet():
    alphabet = {}
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    len_chars = len(chars)

    for i in range(0, len_chars):
        char = chars[i]
        bin_string = bin(i)[2:].zfill(6)
        alphabet[bin_string] = char

    alphabet['0'] = '=' # special code for padding character
    return alphabet
