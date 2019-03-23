import complexity

import random


@complexity.test
def selectionsort(n, shuffle=False):

    c = 1  # cost of the function

    li = list(range(n, 0, -1))

    if shuffle:
        random.shuffle(li)

    for i, x in enumerate(li[:-1]):
        min = i
        for j, y in enumerate(li[i+1:]):
            c += 1
            if y < li[min]:
                min = i+j+1
        if min is not i:
            li[i], li[min] = li[min], li[i]

        c += 1

    return c


complexity.testrange = [10, 100, 1000]

if __name__ == '__main__':

    selectionsort(shuffle=True)