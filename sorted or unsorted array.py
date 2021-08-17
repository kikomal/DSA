def sorted(a):
    x=len(a)
    for i in range(x-1):
        if a[i]>a[i+1]:
            return False
    return True   






a=[1,2,4,5,6,7,9,10]
result=sorted(a)
if result:
    print("Array is sorted")
else:
    print ("Array is not sorted")
