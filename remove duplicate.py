def remove_duplicate(a, x):
    for i in range(x+1):
         if (a[i]-a[i+1])==0:
             
             a.pop(i)
    return a    

x=int(input("Enter the size of array: "))
a=[]
for i in range(x):
    n=int(input("Enter the value of array: "))
    a.append(n)
xyz=remove_duplicate(a, x)
