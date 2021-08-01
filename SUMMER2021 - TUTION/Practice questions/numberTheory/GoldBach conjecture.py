"""
Goldbach conjecture: All even numbers are made out of two prime numbers

"""


def primeornot(x):
    answer = True
    if x==1:
        return False
    else:
        for i in range(2, x//2 +1):
            if x%i==0:
                answer = False
        return answer


def primeranger(start, end):
    answer = []
    for i in range(start, end+1):
        if primeornot(i):
            answer.append(i)
    return answer


def splitter(x):
    if x%2==1:
        a = x//2
        b = (x//2) +1
        return a, b
    else:
        a = x//2
        b = a
        return a, b


def goldbac(number):
    """

    :param number: take in a number
    :return: return combinations of prime number sums
    """
    a, b = splitter(number)
    c = [None, None]
    answer = []
    for i in range(1, number//2):
        if primeornot(a) and primeornot(b):
            c[0] = a
            c[1] = b
            answer.append(c)
        else:
            a+=1
            b = b-1
    answerfinal = []
    for j in answer:
        if j not in answerfinal:
            answerfinal.append(j)
    return answerfinal





def runner():

    print(goldbac(90000))


runner()