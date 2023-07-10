n=int(input())
temp=n

sum=0
while n>0:
    r=n%10
    fact=1
    for i in range(1,r+1):

        fact=fact*i
    sum=sum+fact
    n=n//10
print(sum)
if (temp==sum):
    print("It is strong number")
else:
    print("it is not a strong number")