def print_formatted(number):
    # your code goes here
    bit_l = number.bit_length()
    for i in range(1, number + 1):
        print(
            f"{str(i).rjust(bit_l, ' ')} {oct(i)[2:].rjust(bit_l, ' ')} {hex(i)[2:].upper().rjust(bit_l, ' ')} {(bin(i)[2:]).rjust(bit_l, ' ')}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
