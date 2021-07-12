import math
from itertools import count, islice
import time

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))

def search():
    nums = {1}


    for i in range(1,10000,2):
        for j in range(1, math.ceil(math.sqrt(i)) ):
            if is_prime(i- (2*(j**2))):
                nums.add(i)


    for i in range(1,10000,2):
        if i not in nums:
            if not is_prime(i):
                return i


tick = time.time()
num = search()
tock = time.time()

print(num)
print("Time :", math.ceil((tock - tick) *1000), " ms")