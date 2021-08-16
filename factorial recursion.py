#factorial using recursion
def fact(n):
    if(n==0):  #in order to terminate the recursion at the end we put the end result as 1
        return 1     #by using return 
                      #by using return end funtion that is fact(0) just gave value 1
    return n*fact(n-1)   #and did not called another function as cursor never moved to this line     return n*fact(n-1)




n=int(input("Enter a number: "))
res=fact(n)
print(res)
