n = int(input('How many fibonacci numbers do you want? '))
firstnum = 1
secondnum = 1
if n == 0:
    print ('no number')
elif n==1:
    print (firstnum)
else:
    print (firstnum)
    print (secondnum)

for i in range (3,n+1):
    num= firstnum+secondnum
    print (num)
    firstnum = secondnum
    secondnum = num
