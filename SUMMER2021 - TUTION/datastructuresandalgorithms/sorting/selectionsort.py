"""
selection sort:
 - swapping the first element with the smallest element in the unsorted sublist
"""
y = [3, 2, 6, 1, 9, 4, 1]
     #[1, 2, 6, 3, 9, 4, 1]

def sorter(x):
    for i in range(0, len(x)):
        min = x[i]
        index = i

        for j in range(i, len(x)-1):
            if min > x[i+1]:
                min = x[i+1]
                index = i+1
        x[i], x[index] = x[index], x[i]

    return x

def minlist(x):
    min = 999999999
    for i in range(0, len(x)):
        if x[i]<min:
            min = x[i]

    return min

def indexof(list, x):
    for i in range(0, len(list)):
        if x == list[i]:
            return i




def sorter2(x):
    for i in range(0, len(x)):
        for j in range(1, len(x)):
            if x[i] > minlist(x[j:]):
                minindex = indexof(x[j:], minlist(x[j:]))+i+1
                x[i], x[minindex] = x[minindex], x[i]
    return x


def sorter3(x):
    for i in range(0, len(x)):
        for j in range(1, len(x)):
            minindexinx = indexof(x[j:], minlist(x[j:]))





def runner():
    print(indexof(y, 1))
    # print(sorter2(y))


runner()