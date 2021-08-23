
def rev(num):
  rev = 0
  while num > 0:
    rev = (10*rev) + num%10
    num //= 10
  return rev


def isPalindrome(num):
    return str(num) == str(num)[::-1]

cnt = 0
for n in range(1,10000):
    num = n
    for i in range(50):

        if( isPalindrome(num + rev(num))):
            cnt+=1 
            break
        else:
            num += rev(num)

print(9999-cnt)
