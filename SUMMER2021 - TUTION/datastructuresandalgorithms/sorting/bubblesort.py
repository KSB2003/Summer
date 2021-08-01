"""
Bubble sorting:
 - swap according to 'size'
 - 'nth' heaviest bubble will move to the correct position.
"""
import random as rd


randolist = [rd.randint(1, 100) for n in range(0, 1000)]

def randlist():
    x = []
    for i in range(0, 10000):
        x.append(rd.randint(0, 1000000))
    return x


def sorter(x):
    for i in range(0, len(x)):
        for j in range(0, len(x)-1-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    return x

def runner():
    # print(sorter(randlist()))
    print(randolist)


runner()
