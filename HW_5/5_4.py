# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def encode_file(input_file, output_file):
    input_file = open(input_file, 'r')
    output_file = open(output_file, "w")
    while True:
        line = input_file.readline()
        print(line)
        encoded_val = rle_encode(line)

        output_file.write(encoded_val)

        if not line:
            break

    output_file.close()
    input_file.close()


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


def decode_file(input_file, output_file):
    input_file = open(input_file, 'r')
    output_file = open(output_file, "w")
    while True:
        line = input_file.readline()
        print(line)
        decoded_val = rle_decode(line)

        output_file.write(decoded_val)

        if not line:
            break

    output_file.close()
    input_file.close()


encode_file("text for encode.txt", "encoded text.txt")
decode_file("encoded text.txt", "decoded text.txt")