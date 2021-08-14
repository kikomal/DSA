

def merge(a1, a2, x, y):
    i=0
    j=0
    arr=[]

    while (i<x and j<y):
        if a1[i]<a2[j]:
            arr.append(a1[i])
            i+=1
        else:
            arr.append(a2[j])
            j+=1
    while i<x:
        arr.append(a1[i])
        i+=1
        while j<y:
            arr.append(a2[j])
            j+=1
        


    return arr
a1=[2,4,6,8]
a2=[3,5,7,9,10]
x=len(a1)
y=len(a2)

n1= merge(a1, a2, x, y)

print(n1)
        
      
        
        
    
        
        

    

    
   
        
         
        
