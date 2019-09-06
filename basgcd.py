no1,no2=map(int,input().split())
while(no2!=0):
  temp = no2
  no2 = no1 % no2
  no1 = temp
gcd = no1  
print(gcd)
