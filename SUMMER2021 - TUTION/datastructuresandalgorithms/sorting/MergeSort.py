"""
Merge sort: Divide and conquer type algo.
[9, 1, 3, 6, 5, 0, 8]
[9, 1, 3, 6, 5, 0, 8]
 - list divided into sublists:
 [9, 1, 3] and [6, 5, 0, 8]

 [2, 4, 12] and [1, 8, 9, 11]
 [[3], [2], [5], [4]]

 [[2, 3], [2], [4, 5], [4]]


 [
"""

def minlist(x):
    min = (2**31)-1
    for i in range(0, len(x)):
        if x[i]<min:
            min = x[i]

    return min

def combinesorter(x, y):
    lenx = len(x)
    leny = len(y)
    finalist = [None]*(lenx+leny)
    i, j, k = 0, 0, 0
    while i<len(x) and j<len(y):
        if x[i]<y[j]:
            finalist[k] = x[i]
            i+=1
        elif x[i]>y[j]:
            finalist[k] = y[j]
            j+=1
        else:
            finalist[k], finalist[k+1] = x[i], y[j]
            i+=1
            j+=1

        k+=1
    if i==len(x):
        for l in range(j, len(y)):
            finalist[k] = y[l]
            k = k+1

    else:
        for m in range(i, len(x)):
            finalist[k] = x[m]
            k+=1




    return finalist



def mergesort(x):
    y = [None]*len(x)
    for i in range(0, len(x)):
        y[i] = [x[i]]
    newy = [None]*len(x)
    if len(x)%2==0:
        while len(y)>1:
            a=[]
            for i in range(0, len(y), 2):

                a[i//2] = combinesorter(y[i], y[i+1])
            y = a
            print(y)




def mergesort2(myList):
    y = [[myList[i]] for i in range(0, len(myList))]
    while len(y) > 1:

        a = []
        for i in range(0, len(y), 2):
            try:
                a.append(combinesorter(y[i], y[i + 1]))
            except IndexError:
                a.append(y[i])
        y = a
    return y[0]










def runner():
    print(mergesort2([2, 1, 5, 4, 1]))




runner()