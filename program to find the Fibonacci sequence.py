number= int(input('Enter the number how many terms: '))
a=0
b=1
for i in range(number):
    print(a, end=',')
    b,a=a+b, b
    
