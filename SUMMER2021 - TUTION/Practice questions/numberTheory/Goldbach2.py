import math
from datetime import datetime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def goldbach_till(n):
    results = {}
    for j in range(n, n+1, 2):
        for i in range(2, j//2 + 1):
            if is_prime(i) and is_prime(j-i):
                results[j] = (i, j-i)
                break
    return results


def runner():
    t1 = datetime.now()
    limit = 100000000
    answer = goldbach_till(limit)
    print(answer)
    t2 = datetime.now()
    print(f"time taken: {t2 - t1}, limit : {limit}")

runner()

