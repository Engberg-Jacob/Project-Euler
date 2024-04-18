import array
import numpy as np

i = 0

if i <= 1000:
    if i % 3 == 0 or i %  5 == 0:
        sum = 0
        sum = sum + i
    i = i + 1

print(sum)



def f(a, b):
    while a <= 1000:
        if (a % 3 )== 0 or (a % 5) == 0:
            b = b + a
        a = a + 1
    print(b)


f(0, 0)
