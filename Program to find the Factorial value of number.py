number =int(input('Enter the value of number: '))
factorial=1

##Use for loop
# for i in range(1, number+1):
#     factorial=factorial*i
# print('The factorial of',number, 'is', factorial)

##Use while loop
i=1
while i<=number:
    factorial*=i
    i+=1
print('The factorial of', number, 'is', factorial)