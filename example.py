import complexity
import random


# the first parameter has to be n
def selectionsort(n, shuffle=False, generator=lambda n: list(range(n, 0, -1))):

    c = 1  # cost of the function

    li = generator(n)

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


if __name__ == '__main__':
    # add function to the test queue, the function has to return the total costs
    complexity.queue(selectionsort, shuffle=True)

    # runs all tests compared to selectionsort
    complexity.test(selectionsort)