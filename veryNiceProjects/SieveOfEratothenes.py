from math import isqrt

primes_list = []

# gets primes up to but not including this number
n = 100

# edge cases
if n<=2:
    print([])
primes = [True] * n
primes[0] = False
primes[1] = False

# found all primes
for i in range(2, isqrt(n)):
    if primes[i]:
        for j in range(i*i, n, i):
            primes[j] = False

# printing primes
for num in range(len(primes)):
    if primes[num]:
        primes_list.append(num)

print(primes_list)