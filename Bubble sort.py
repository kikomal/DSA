def sort(a1, size):
    i=0
    j=0
    
    for i in range(size):
        for j in range(0,size-i-1):
            if a1[j]>a1[j+1]:
                temp=a1[j]
                a1[j]=a1[j+1]
                a1[j+1]=temp
    return a1         
                














a1=[5,8,2,6,7]
size=len(a1)
a=sort(a1, size)
print(a)
