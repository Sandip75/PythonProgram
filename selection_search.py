def s_sort(a):
    for i in range(0,len(a)-1):
        minindex = i
        for j in range(i+1 ,len(a)):
            if(a[j] < a[minindex]):
                minindex = j
        if minindex != i :
            a[i] , a[minindex] = a[minindex] , a[i]
        
                                

a = [ 3,5,1,65,17,323,23]
s_sort(a)
for i in range(len(a)):
    print ("%d " %a[i])
