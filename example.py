import complexity


@complexity.test
def algodat_01_5b(n):
    c = 1  # cost of the function

    i = 1
    x = 1

    while i < n:
        a = 4*i
        for j in range(int(a), 1, -1):
            x = x+j
            c += 1
        i = a/2
        c += 1

    return c  # returns the costs


if __name__ == '__main__':

    algodat_01_5b()