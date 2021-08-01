
def combination(n, r):
    a = n-r
    b = r
    c = None
    d = None
    if a>=b:
        c = a
        d = b
    else:
        c = b
        d = a

    fac = n

    for i in range(n-1, c, -1):
        fac = fac*i
    fac1 = 1
    for j in range(1, d+1):
        fac1 = fac1*j

    return fac/fac1

def combination2(n, r):
    r = min(r, n-r)
    num = 1
    den = 1

    for i in range(1, r+1):
        num = num*(n-i+1)
        den = den*i

    return num//den





"""
5 and 2

a = 3
b = 2

c = a = 3
d = b  = 2

fac = 5
5*4*3*2
"""

def runner():
    print(combination(6, 4))


runner()

"""
fermats last theorem
dynamic programming meaning


sigma ncr, r should go from 0 to n,  2**n
do lambda for ncr

do function without lambda for sum
do with lambda

"""