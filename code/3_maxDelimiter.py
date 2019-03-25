# 3) Каков самый большой делитель числа 600851475143, являющийся простым числом?
import math


def issimple(a):
    q = math.ceil(math.sqrt(a))
    lst = []
    for i in range(2, q):
        if a % i == 0:
            if not issimple(i):
                lst.append(i)
    return lst


r = issimple(600851475143)
print(max(r))
