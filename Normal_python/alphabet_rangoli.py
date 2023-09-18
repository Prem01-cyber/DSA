def print_rangoli(size):
    # your code goes here
    import string

    alpha = string.ascii_lowercase
    for i in range(size-1, 0, -1):
        s = "-".join(alpha[i:size])
        print((s[::-1]+s[1:]).center(4*size-3, "-"))
    for i in range(size):
        s = "-".join(alpha[i:size])
        print((s[::-1]+s[1:]).center(4*size-3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)