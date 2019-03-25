# 7) Какое число является 10001-ым простым числом?

import math

i = 6
a = 13

while i != 10001:
    a += 1
    q = math.ceil(math.sqrt(a)) + 1
    fl = True
    for j in range(2, q):
        if a % j == 0:
            fl = False
    if fl:
        i += 1
print(a)
