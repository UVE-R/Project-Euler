
def split(n):

    x = set()
    for i in str(n):
        x.add(int(i))


    return x


for i in range(1,1000000):
    if(split(2*i) == split(3*i)):
        if(split(2*i) == split(4*i)):
            if( split(2*i) == split(5*i)):
                if( split(2*i) == split(6*i)):
                    print(i)
                    
