"""
linear/sequential sorting: 1 by 1 comparision
"""


def searcher(x, xlist):
    answer = False
    counter = 0
    for i in range(0, len(xlist)):
        if x==xlist[i]:
            answer = True

            break
        counter+=1


    if answer:
        return answer, counter
    else:
        return answer



def finalrunner():
    print(searcher(5, [1, 2, 3, 4, 5]))


finalrunner()