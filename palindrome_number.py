n=int(input("Enter the number"))
temp=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("reverse of a given number",rev)
if(temp==rev):
    print("Given number is palindrome")
else:
    print("It is not a palindrome")
    
