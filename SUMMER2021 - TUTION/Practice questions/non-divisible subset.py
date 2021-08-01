
"""
create the largest subset such that all paired sum of numbers is not divisible by k

"""


def factorial(n):
    product = 1
    for i in range(1, n+1):
        product*=i
    return product


def combination(n, r):
    answer = factorial(n)/(factorial(n-r)*factorial(r))
    return int(answer)


def finalfunction(x, k):
    remainderlist = []
    for i in x:
        remainderlist.append(i%k)

    remaindermapper = {}
    for j in range(0, k):
        remaindermapper[j] = 0

    for vals in remainderlist:
        remaindermapper[vals]+=1
    counter = 0
    for m in range(1, (k+1)//2):
        if remaindermapper[m]>remaindermapper[k-m]:
            counter+=remaindermapper[m]

        else:
            counter+=remaindermapper[k-m]

    if remaindermapper[0] != 0:
        counter+=1

    if k%2==0:
        if remaindermapper[k//2] != 0:
            counter+=1

    return counter




def runner():
    print(finalfunction([4, 8, 12], 4))


runner()