def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        print(str(i).rjust(len(bin(number)[2:])), end=' ')
        print(str(oct(i))[2:].rjust(len(bin(number)[2:])), end=' ')
        print(str(hex(i))[2:].upper().rjust(len(bin(number)[2:])), end=' ')
        print(str(bin(i))[2:].rjust(len(bin(number)[2:])), end=' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)