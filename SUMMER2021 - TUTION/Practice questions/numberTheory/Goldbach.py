"""
Goldbach conjecture: All even numbers are made out of two prime numbers
"""
from datetime import datetime
import csv


def primeornot(x):
    answer = True
    if x==1:
        return False
    else:
        for i in range(2, x//2 +1):
            if x%i==0:
                answer = False
                break
        return answer


# def primeranger(start, end):
#     answer = []
#     for i in range(start, end+1):
#         if primeornot(i):
#             answer.append(i)
#     return answer


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
    """
    a => 8 9 10 11
    b => 8 7 6 5
    c = [ , ]
    """
    a, b = splitter(number)
    answer = []
    for i in range(1, number//2):
        c = [None, None]
        if primeornot(a) and primeornot(b):
            c[0] = a
            c[1] = b
            answer.append(c)
        a+=1
        b = b-1
    answerfinal = []
    for j in answer:
        if j not in answerfinal:
            answerfinal.append(j)
    return answerfinal

def goldbachchecker(x):
    a, b = splitter(x)
    answer = False
    c = [None, None]
    for i in range(1, x//2):
        if primeornot(a) and primeornot(b):
            answer = True
            c[0], c[1] = a, b
            break
        a-=1
        b+=1

    return answer, c


def runner():
    # num = 100000
    # start_time = datetime.now()
    # answer = goldbac(num)
    # end_time = datetime.now()
    # print(f"time taken : {end_time-start_time}")
    #
    # file = open(f"GoldbachResults/{num}.csv", "w")
    # writer = csv.writer(file)
    # for pair in answer:
    #     writer.writerow(pair)
    # writer.writerow(["time taken", end_time-start_time])
    # file.close()
    start_time = datetime.now()
    print(goldbachchecker(100000000))
    end_time = datetime.now()
    print(f"The time taken is {end_time-start_time}.")


runner()