n=int(input("Enter number: "))
reve=0
while(n>0):
    digi=n%10
    reve=reve*10+digi
    n=n//10
print("Reverse of the number:",reve)
