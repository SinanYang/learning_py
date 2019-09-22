import math


def prime(num):
    pri = True
    if num == 1:
        pri = False
        return pri
    else:
        i = 2
        while i <= math.sqrt(num):
            if num % i == 0:
                pri = False
                break
            i += 1
        return pri


def monisen(no):
    m = 0
    count = 0
    i = 1
    while count < no:
        if prime(i):
            m = pow(2, i) - 1
            if prime(m):
                count += 1
        i += 1

    return m


print(monisen(int(input())))
# successfully run
