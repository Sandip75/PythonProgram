
def b_search(a ,l ,r ,x):
    
    if r>=l:
        mid = int(l +(r-l)/2)
        if (a[mid] == x):
            return mid
        elif (a[mid] > x):
            return b_search(a,l,mid-1,x)
        else:
            return b_search(a,mid+1,r,x)
    else:
        return -1
    
            
    
        

a = [1,5,2,5,2,6,23]
x = 1

re = b_search(a ,0 , len(a)-1 ,x)

if re ==-1:
    print ("The element is not found ")
else:
    print ("The element is at index %d" %(re))
