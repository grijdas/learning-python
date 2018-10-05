num = int(input('Enter a positive number. Enter 0 to end: '))

output = 0
for i in range(1, num+1):
    if num % i == 0:
        print(i)
        output = output + i

print('The sum of divisors is:'+ str(output))

