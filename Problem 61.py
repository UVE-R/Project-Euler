import itertools
import time

three = []
four = []
five = []
six = []
seven = []
eight = []

start = time.time()

#generate number types
for i in range(0, 10000):

    tri = int((i*(i+1))/2)
    if len(str(tri)) == 4:
        three.append(tri)

    squ = i**2
    if len(str(squ)) == 4:
        four.append(squ)

    pent = int((i*((3*i)-1))/2)
    if len(str(pent)) == 4:
        five.append(pent)

    hex = int((i*((2*i)-1)))
    if len(str(hex)) == 4:
        six.append(hex)
    
    hept = int((i*((5*i)-3))/2)
    if len(str(hept)) == 4:
        seven.append(hept)

    octag = int(i*((3*i)-2))    
    if len(str(octag)) == 4:        
        eight.append(octag)


lists = [four, five, six, seven, eight]
nums = [0, 1, 2, 3, 4]

#return all cyclic matches of a number, n , in a list of numbers, nums.
def find(n, nums):
    
    ans = []
    for num in nums:
        if str(num)[0:2] == str(n)[2:]:
            ans.append(num)

    return ans

#recursively searches for cyclic numbers by going through all permuations
#returns a list of the numbers found
def search(current, perm, depth):

    if depth == 6:
        return [current]

    matches = find(current, lists[perm[0]]) #find number which is will form part of a cycle with current

    if len(matches) > 0:
        for i in matches:
            return [current] + search(i, perm[1:], depth+1) 
    else:
        return [0]

for i in three: #starting with the Triangle number set for the start of the cycle
    for j in list(itertools.permutations(nums)): # for each permutation of the remaining number sets    
        x = search(i, j, 1)
        if(len(x) >=5):
            if 0 not in x:
               if str(x[5])[2:] == str(x[0])[0:2]: #check if the first and last number in the list will form a complete cycle
                   print(x)
                   end = time.time()
                   print("Answer is", sum(x), ", found in", round(end - start, 2), "seconds")
