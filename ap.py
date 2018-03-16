def Nth_of_AP(a, d, N) :
 
   
    return (a + (N - 1) * d)
      
  

a = int(input('enter the number'))
d = int(input('enter the number' )) 
N = int(input('enter the number'))  
sum=0
while(N>0):
  sum += N
  N -= 1
print(sum)
 
