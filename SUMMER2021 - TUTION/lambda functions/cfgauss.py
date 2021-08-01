
def adder(x, y):
    return x+y





addervar = lambda x, y: x*y

sumlema = lambda n: n*(n+1)/2

sumnoddnums = lambda x: x*x



def gausschecker(function, limit = 5):

    for i in range(1, limit):
        if normaladder(i) != function(i):
            return False
    else:
        return True



def normaladder(x):
    sum = 0
    for i in range(1, x+1):
        sum+=i

    return sum




def runner():
    # print(gausschecker(sumlema))
    print(sumnoddnums(5))



runner()