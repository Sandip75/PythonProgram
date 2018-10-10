##def i_sort(a):
##    for i in range(1,len(a)):
##        for j in range(i-1 ,-1 ,-1):
##            if(a[j]>a[j+1]):
##                a[j] , a[j+1] = a[j+1] , a[j]
##            else:
##                break
##            


def i_sort(a):
    for i in range(1,len(a)):
        c = a[i]
        for j in range(i-1 ,-1 ,-1):
            if(a[j]>c):
                a[j+1] = a[j]
            else:
                a[j+1]=c
                break

a = [ 3,5,1,65,17,323,23]
i_sort(a)
for i in range(len(a)):
    print ("%d " %a[i])
