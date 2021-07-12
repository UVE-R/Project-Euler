#Not optimal solution
import math
from itertools import count, islice
import time

#checks if a number is prime
def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))

def search():
    nums = {1} #holds all of the composite odd numbers which satisfy the condition
    
    #find all prime odd composite numbers which satisfy the equation
    for i in range(1,10000,2): 
        for j in range(1, math.ceil(math.sqrt(i))):
            if is_prime(i- (2*(j**2))): 
                nums.add(i) 
    
    #find the first odd composite
    for i in range(1,10000,2):
        if i not in nums:
            if not is_prime(i):
                return i

tick = time.time()
num = search()
tock = time.time()

print(num)
print("Time :", math.ceil((tock - tick) *1000), " ms")
