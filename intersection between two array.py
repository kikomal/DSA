
def intersection(a,b):
    res=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                res.append(a[i])
                break
    return res













a=[1,3,4,5,7]
b=[2,4,5,7,8,10]
print(intersection(a,b))
