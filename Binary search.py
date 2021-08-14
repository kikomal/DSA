#binary search program
def search(a,key,n):
    i=0
    j=n-1
    flag=0
    while i<j and flag==0:
            mid=(i+j)//2
            if key==a[mid]:
                print("The searched value is found at position ", mid+1)
                flag=1
            if key<a[mid]:
                j=mid
            if key>a[mid]:
                i=mid




a=[]
n=int(input("Enter the size of the array: "))
for i in range(n):
    val=int(input("Enter the value of array: "))
    a.append(val)
key=int(input("Enter the number that you want to search: "))

search(a, key, n)

    
