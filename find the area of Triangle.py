import math
a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
c=int(input('Enter the value of c: '))
s=(a+b+c)/2
if (a+b)>c and (b+c)>a and (a+c)>b:
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('Area of Triangle: ',area)
else:
    print('Triangle is not possible')