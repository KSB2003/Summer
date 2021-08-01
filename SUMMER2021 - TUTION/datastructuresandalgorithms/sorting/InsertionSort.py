"""
Insertion sort:
 - goal: after n passes the first n elements should be sorted.

 - [3, 2, 7, 1, 9]
 - [3|, 2, 7, 1, 9]
 - [2, 3|, 7, 1, 9]
 - [2, 3, 7|1, 9]
 - [1, 2, 3, 7|9]
 - [1, 2, 3, 7, 9|]

"""


"""
HW:
- do without creating new list - manipulate the original list.
- CAN create a temp variable during manipulation.
- use only 2 loops NOT 3 
"""


x = [3, 2, 7, 1, 9]

def printer(x):
    for i in range(len(x)-1, -1, -1):
        print(x[i])

def inserter(position, value, x):
    x.append(76)
    for i in range(len(x)-1, position-1, -1):
        x[i] = x[i-1]
    x[position] = value
    return x




def ascendingadd(x, xlist):
    if isinstance(xlist, list):
        inserted = False
        for i in range(0, len(xlist)):
            if x<xlist[i] or x==xlist[i]:
                inserter(i, x, xlist)
                inserted = True
                break

        if inserted == False:
            xlist.append(x)


        return xlist


def sorter(x):
    addon = []
    for i in range(0, len(x)):
        addon = ascendingadd(x[i], addon)
        print(addon)
    return addon


"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
 - [3, 2, 7, 1, 9]
 - [3|, 2, 7, 1, 9]
 - [2, 3|, 7, 1, 9]
 - [2, 3, 7|1, 9]
 - [1, 2, 3, 7|9]
 - [1, 2, 3, 7, 9|]
"""
element = 14
finalist = [3, 2, 7, 1, 9]
def insertionsorter(xlist):
    pass






"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

def trialrunner():
    # print(ascendingadd(3, [1, 2, 3, 4, 5]))
    # print(inserter(0, 84, x))
    pass


def finalrunner():
    print(sorter(x))


finalrunner()