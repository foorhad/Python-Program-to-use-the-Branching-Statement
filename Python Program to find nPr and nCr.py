import math
n=int(input('Enter the value of n: '))
r=int(input('Enter the value of r: '))
npr=math.factorial(n)/math.factorial(n-r)
ncr=(math.factorial(n)/math.factorial(n-r))/math.factorial(r)
print('nPr=',npr)
print('nCr=',ncr)