# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


name = input('What is your name?')
age = int(input('What is your age?'))
old = str((2018-age)+100)

print('{0} will be 100 years old in the year {1}'.format(name, old))
