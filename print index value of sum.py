n=int(input("Enter the size of nums:"))
nums=[]
for i in range(n):
    n=int(input("Enter the value "))
    nums.append(n)
target=int(input("Enter the value of target: "))    


ans=[]
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i]+nums[j]== target:
            ans=[i,j]
            print(ans)
         
