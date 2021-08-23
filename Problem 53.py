from math import ceil
from math import factorial as fact

cnt = 0

def comb(n,r):
    f = fact
    return f(n) / f(r) / f(n-r)

for i in range(1,101):

    for j in range(0,i+1):
        
        if(comb(i,j)> 1000000):
            cnt+=1

print(cnt)
