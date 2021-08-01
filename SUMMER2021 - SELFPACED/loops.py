"""

for loops:
 - iterates through the individual things in a specific data, for example in a string the loop iterates through the characters.
 - thje same is true in lists, for loops iterate through the individual elements in a list.

"""

"""
continue operator:
 - It is the opposite of break statements, the function/loop will continue even if there is a continue statement.
 - It should be used in loops 
"""


"""

Mutable: 
 - this means that the data in the list can me modified. 
 
Immutable:
 - This means that the data inside of the list cannot be modified. 

 """


def charprinter(x):
    for char in x:
        print(char)


def inserter(position, value, x):
    a = []
    b = []
    for i in range(0, position):
        a.append(x[i])


    for j in range(position, len(x)):
        b.append(x[j])

    a.append(value)
    return a+b


def runner():
    print(inserter(3, 5, [2, 1, 3, 9]))



runner()