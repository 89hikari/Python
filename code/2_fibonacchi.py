# 2) Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона
one = 1
two = 2
elem = 0
count = 2
while elem < 4000000:
    elem = one + two
    one = two
    two = elem
    if elem % 2 == 0:
        count += elem
print(count)
