def printStar(num):
    if num <= 0 or num > 20:
        print("invalid input")
    else:
        output = ''
        for num in range(1, num + 1):
            output = output + '*'
        print(output)


num = int(input('Enter a number between 1 and  20. Enter 0 to end:  '))
printStar(num)

