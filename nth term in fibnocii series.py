num=int(input("Enter a number"))
n1=0
n2=1
l=[0,1]
print("fibnocii series :",n1,n2 , end="  " )
for i in range(2,num):
    n3=n1+n2
    l.append(n3)
    n1=n2
    n2=n3
    print(n3,end=" ")


    
print(l)
print(l[3])

