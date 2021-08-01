

"""
1634 = 1**4 + 6**4 + 3**4 + 4**4

"""


def checker(x):
    x = str(x)
    power = len(x)
    sum = 0
    for i in range(0, len(x)):
        sum+=int(x[i])**power

    return sum==int(x)

def ranger(start, end):
    answer = []
    for i in range(start, end+1):
        if checker(i):
            answer.append(i)

    return answer

def runner():
    print(checker(153))
    print(ranger(1, 200000))

runner()