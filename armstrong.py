n=int(input("enter a number"))
summ=0
temp=n
while(n>0):
    r=n%10
    summ=summ+r*r*r
    n=n//10
print(summ)
if(summ==temp):
    print("it is a armstrong")
else:
    print("it is not a armstrong")
    
