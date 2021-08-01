import random as rd


def randomReturner():
    x = rd.randint(1, 6)
    return x

def probChecker(n, games):
    sample = [0]*n
    for i in range(0, games):
        player = 0
        while randomReturner() != 6:
            player = (player+1)%n
        sample[player] += 1
    for j in range(0, len(sample)):
        sample[j] = sample[j]/games
    return sample


def runner():
    print(probChecker(3, 1000000))



runner()

