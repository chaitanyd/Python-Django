def print_rangoli(size):
    # your code goes here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lines = []  # empty list to store our output
    for row in range(size):  # this loop for looping withing range
        print_ = "-".join(alpha[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])

    for row in range(size - 1, 0, -1):  # this loop for printing lower part
        print(lines[row].center(width, '-'))

    for row in range(size):  # this loop is for printing upper part
        print(lines[row].center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)