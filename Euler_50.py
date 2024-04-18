import Euler_10 as sieve
import itertools as it
import time
from operator import itemgetter

def acu_sum(x):
    i = 0
    for number in range(len(x)):
        i += x[number]
        #print (i, number)
        yield (i, number)


def prime_con(n):
    primes = sieve.second_sieve(n)
    print(primes)
    consecutive_primes = [x for x in acu_sum(primes) if x[0] in primes]
    print(consecutive_primes)
    for i in primes:
        print("NEW LOOP", i)
        primes = primes[1:]
        consecutive_primes = consecutive_primes + [x for x in acu_sum(primes) if x[0] in primes[1:]]
        print(primes)
        print(consecutive_primes)
    print(primes)
    print(consecutive_primes)




def acu_sum2(x):
    i = 0
    for number in range(len(x)):
        i += x[number]
        #print (i, number)
        yield number
    



def prime_con2(n):
    primes_to_check = sieve.second_sieve(n)
    primes_to_sum = prime_sum(n,primes_to_check)
    prime=[(0,0)]
    for i in range(len(primes_to_sum)):
        slices_of_primes = primes_to_sum[i:]
        consecutive_primes = [(i,x) for i,x in enumerate(it.accumulate(slices_of_primes)) if x in primes_to_check]
        longest_prime = max(consecutive_primes, key=itemgetter(0))
        if longest_prime[0] > prime[-1][0]:
            prime.append(longest_prime)
    return max(prime, key=itemgetter(0))

def prime_sum(n,primes):
    temp=0
    count=0
    for i in range(len(primes)):
        temp += primes[i]
        count+=1
        if temp > n:
            break
    return primes[:count]

#print(prime_con2(1000000))
# Korrekt, 522 sek = 8.7 min, prim = 997651, sumlængde = 543

start_time = time.time()
def prime_sum2(n):
    primes_to_check = sieve.second_sieve(n)
    primes_to_sum = prime_sum(n,primes_to_check)
    cumulative_sum = list(it.accumulate(primes_to_sum[:-1]))
    n = len(cumulative_sum)
    cumulative_primes = []
    for i in range(1,len(cumulative_sum)+1):
        if cumulative_sum[-i] in primes_to_check:
            cumulative_primes.append((cumulative_sum[-i], n-i+1))
        for j in range(len(cumulative_sum)):
            if cumulative_sum[-i]-cumulative_sum[j] in primes_to_check:
                cumulative_primes.append((cumulative_sum[-i]-cumulative_sum[j], n-i+1))
    print(cumulative_primes)
    return max(cumulative_primes, key=itemgetter(1))[0]
    #18 min, korrekt svar



print(prime_sum2(1000000))
print("--- %s seconds ---" % (time.time() - start_time))