n=int(input())
def getSum(n): 
   
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return sum
def getProduct(n): 
  
    product = 1
  
    while (n != 0): 
        product = product * (n % 10) 
        n = n // 10
  
    return product 
k=getSum(n)+getProduct(n)
if(k==n):
  print("Great")
else:
  print("no")
