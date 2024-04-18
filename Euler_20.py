import math
import time
start_time=time.time()
def cross_sum(n):
    q = 0
    digits = []
    exponent = 1
    while n > q:
        i = n%(10**exponent)
        digits.append((i-q)/(10**(exponent-1)))
        q = i 
        exponent = exponent + 1
    return(sum(digits))

print(cross_sum(math.factorial(100)))
print("--- %s seconds ---" % (time.time() - start_time))
#Pas på for store tal?