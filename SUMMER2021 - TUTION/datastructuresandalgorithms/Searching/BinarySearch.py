import random as rd
"""
Binary search: needs a sorted list.
time complexity is log n to base 2

"""
"""
implement binary search recursively
"""

def searcher(x, sortedlist):
    low = 0
    high = len(sortedlist)-1
    answer = False
    while low<=high:
        mid = (low+high)//2
        if sortedlist[mid]==x:
            answer = True
            return answer, mid
        elif sortedlist[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return answer


x = 6
xlist = [1, 4, 5, 9, 11]

#662
def binarygame():
    print("You have 10 guesses to guess a random number between 1 to 1000!")
    number = rd.randint(1, 1000)
    print(str(number) +" - don't cheat, only for the computer!!!")
    maz = 1000
    min = 1
    answer = False
    for i in range(0, 10):
        guess = int(input("Enter your guess between 1 and 1000: "))
        if guess > number:
            print("Too big, try smaller!")
        elif guess < number:
            print("Too small, try another number")
        else:
            print("Yay you have guessed the number!!")

            answer = True
            break

    if not answer:
        print("Sorry loser, the number was "+str(number)+".")




def finalrunner():
    # print(searcher(x, xlist))
    binarygame()


finalrunner()