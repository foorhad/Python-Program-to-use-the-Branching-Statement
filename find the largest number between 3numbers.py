num1=int(input('Enter the first number: '))
num2=int(input('Enter the first number: '))
num3=int(input('Enter the first number: '))
if num1>num2 and num1>num3:
    largest=num1
elif num2>num3:
    largest=num2
else:
    largest=num3
print(largest, 'is the largest number between', num1, ',', num2, '&', num3)