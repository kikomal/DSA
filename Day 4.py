def search(num, n, a):
    for i in range(n):
        if a[i]==num:
            pos=i
            print("Given value is found at", pos+1)
            break
    
    print("Number not found")

n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    val=int(input("Enter the value in array: "))
    a.append(val)
num=int(input("Enter the value that you want to search: "))


search(num, n, a)
    
