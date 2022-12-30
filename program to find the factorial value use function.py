# import math
# number=int(input('Enter the value of number: '))
# factorial = math.factorial(number)
# print('The factorial of ', number, 'is', factorial)

##Manually use function
def fact(x):
    factorial=1
    for i in range(1,x+1):
        factorial*=i
    return factorial    

x=int(input('Enter the value of x: '))
fa =fact(x)
print(fa)