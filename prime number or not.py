n=int(input())
count=1
if n==1:
    print("it is not a prime number")
elif (n<0):
    print("its not a prime number")
else:
        for i in range(2,n):
              if(n%i==0):
                count=count+1
        if(count==1):
            print("it is a prime number")
        else:
            print("It is not  a prime number")