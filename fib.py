num= int(input('Write your number ' ))

numberone =1
numbertwo =1

if num == 1 and num == 2:
    print(num/num)


elif num <= 0:
    print ('This number is not a valid number')

else:
    for i in range (3, num+1):
        out = numberone+numbertwo
        numbertwo = numberone
        numberone = out

        if i == num:
            print(out)

