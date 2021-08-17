def union(a,b):
    i=j=0
    res=[]
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            res.append(a[i])
            i+=1
            j+=1
        elif a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    return res       










a=[1,2,4,8,9,10]
b=[2,3,5,6,8,11,15]
print(union(a,b))
