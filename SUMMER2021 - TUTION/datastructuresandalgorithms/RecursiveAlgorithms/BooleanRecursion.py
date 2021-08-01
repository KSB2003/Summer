"""
 - take in a list of booleans
    - return true if all of the elements are true
    - else return false


HW:
 - given a list of integers such that all numbers except for a particular number occur in pair,
  write a recursive function to return the number that occurs only once.

  hint: XOR gate - associative property
  """

x = [True, True, True, True, True]
x1 = [True, False, True, False, True]

def boolrecursion(x):
    if len(x)==1 and x[0]==True:
        return True

    elif len(x)==1 and x[0]==False:
        return False

    else:
        return boolrecursion(x[1:]) and x[0]






def runner():
    print(boolrecursion(x))


runner()