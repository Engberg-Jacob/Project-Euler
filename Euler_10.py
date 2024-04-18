import numpy as np
import math



#first attempt. correct, time to optimize
def first_sieve(n):
    numbers = []
    for i in range(2, n+1):
        numbers.append(i)
    prime_stop = math.ceil(np.sqrt(n))
    smallest_prime_index = 0
    while numbers[smallest_prime_index] <= prime_stop:
        smallest_prime = numbers[smallest_prime_index]
        indeks_to_be_removed =[]
        for i in range(smallest_prime_index + 1, len(numbers)):
            if (numbers[i] % smallest_prime) == 0:
                indeks_to_be_removed.append(i)
#        numbers = [v for i, v in enumerate(numbers) if i not in indeks_to_be_removed]
        for indeks in sorted(indeks_to_be_removed, reverse=True): #Reverse because otherwise you remove indices before you get to them
            del numbers[indeks]
        smallest_prime_index = smallest_prime_index + 1
    return numbers #As is: Gives correct answer, 142913828922, but only after 597 sec = 10 min



def second_sieve(n):
    numbers = []
    for i in range(2, n+1):
        numbers.append(i)
    prime_stop = math.ceil(np.sqrt(n))
    smallest_prime_index = 0
    while numbers[smallest_prime_index] <= prime_stop:
        smallest_prime = numbers[smallest_prime_index]
        numbers = [x for x in numbers if not x % smallest_prime == 0 or x == smallest_prime]
        smallest_prime_index = smallest_prime_index + 1
    return numbers #As is: Gives correct answer, 142913828922, after 6 sec

#n = 2000000

#number_list2 = second_sieve(n)
#summed2 = 0
#for i in number_list2:
#    summed2 = summed2 + i
#print(summed2)

# Har lært om list comprehension