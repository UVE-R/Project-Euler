import math
import time

#Brute force through all positibities of a,b and c
def sol1():
    tick = time.time()

    for a in range(1000):
        for b in range(1000):
            c = math.sqrt(pow(a,2) + pow(b,2))

            if a==0 or b == 0:
                continue
            elif a+b+c == 1000:
                tock = time.time()
                return math.floor(a*b*c), tock - tick


#Optimization of the brute force method which does not check duplicate combinations of a and b
def sol2():
    
    def checkTriple(a,b,c):
        return a**2 + b**2 == c**2

    tick = time.time()

    for a in range(1000):
        for b in range(a, 1000-a):
            c = 1000 - (a+b)

            if c<b or c<a or a==0 or b==0:
                break
            else:
                if checkTriple(a,b,c):
                    tock = time.time()
                    return math.floor(a*b*c), tock - tick                   

    
def main():

    sol,time  = sol2() #change depending on the solution

    print("Solution: ",sol, "Time: ",time * 1000," ms")

main()
                
