

def linear_search(a , x):
    
    for i in range(len(a)):
        if a[i]==x:
            return i
        
    return -1








a = [1,5,2,5,2,6,23]
x = 2


re = linear_search(a ,x)

if re ==-1:
    print ("The element is not found ")
else:
    print ("The element is at index %d" %(re))
