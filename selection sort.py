#selection sort array
def selcsort(a, m):
    i=0
    for i in range(m):
        mid=a[i]
        for j in range(i+1, m):
            if mid> a[j]:
                temp=mid
                mid=a[j]
                a[j]=temp
        a[i]=mid
        print(a)
    return a



a=[8,1,5,9,6,7,3]
m=len(a)
selcsort(a, m)
print(a)
