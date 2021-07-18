import math
from collections import Counter
import time

#Sieve to generte prime numbers up to n
def Sieve(n):

    primes = [1] * (n+1)
    primes[0] = 0
    primes[1] = 0

    for i in range(2, int(math.sqrt(n+1))) :
        if primes[i] == 1:
            j =2 
            while i*j <= n:
                primes[i*j] = 0
                j += 1

    prime_list = []
    for i in range(2, n):
        if primes[i] == 1:
            prime_list.append(i)

    return  prime_list

#return list of prime families
def prime_families(n):
    num = str(n)
    family = []

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in (Counter(num) - Counter(set(num))): #for each duplicate 
        f = []
        for d in digits:
            f.append( int(num.replace(x,d)))
            family.append(f)

    return family

checkednums = [] #holds numbers we have checked for primality
#remove non-primes from a list 
def check(plist):
    for i in plist:
        checkednums.append(i)
        if i not in primes:
            plist.remove(i) #remove the number if it is not prime 
    return plist


tick = time.time()
allprimes = Sieve(1000000)
primes = []

#find primes with 3 or more repeated characters
for x in allprimes:
    if len(str(x)) - len(set(str(x))) >=3:
        primes.append(x)

run = True  
i=0
while run:
    if primes[i] not in checkednums:
        family = prime_families(primes[i])
        for j in family:
            if len(check(j)) == 8:
                print(j[0])
                run = False
                tock = time.time()
                break
    i += 1


print("Time :", (tock - tick) * 1000, " ms")

