#Challenge 12
print('Challenge 12\n\n')

num=int(input('Give me a number.\n'))
num2=int(input('Give me another number.\n'))

if num2 > num:
    print(num,num2)
else:
    print(num2,num)

#Challenge 13
print('Challenge 13\n\n')

num=int(input('Give me a number under 20.\n'))
if num >= 20:
    print('Too high.')
else:
    print('Thank you.')

#Challenge 14
print('Challenge 14\n\n')

num=int(input('Give me a number between 10 and 20.\n'))
if num >= 10 and num <= 20:
    print('Thank you.')
else:
    print('Incorrect answer.')

#Challenge 15
print('Challenge 15\n\n')

colour=input('What is your favoutire colour?\n')
if 'red' in colour:
    print('I like red too.')
elif 'Red' in colour:
    print('I like red too.')
elif 'RED' in colour:
    print('I like red too.')
else:
    print(f"I don't like {colour} I prefer red.")

#Challenge 16
print('Challenge 16\n\n')

rain=input('Is it raining?\n')
if 'yes' in rain:
    wind=input('Is it windy?\n')
    if 'yes' in wind:
        print('Too windy for an umbrella.')
    else:
        print('Take an umbrella.')
else:
    print('Enjoy your day.')

#Challenge 17
print('Challenge 17\n\n')

age=int(input('How old are you?\n'))
if age >= 18:
    print('You can vote.')
elif age == 17:
    print('You can learn to drive.')
elif age == 16:
    print('You can learn to drive a car.')
else:
    print('You can go trick-or-treating.')

#Challenge 18
print('Challenge 18\n\n')

num=int(input('Give me a number.\n'))
if num < 10:
    print('Too low.')
elif num >=10 and num <= 20:
    print('Correct')
else:
    print('Too high.')

#Challenge 19
print('Challenge 19\n\n')

num=int(input('Enter either 1,2 or 3.\n'))
if num == 1:
    print('Thank you.')
if num == 2:
    print('Well done.')
if num == 3:
    print('Correct.')
else:
    print("Error message (can't read)")

#Challenge 35
print('Challenge 35\n\n')

name=input('Enter your name.\n')
print('\n')
for i in range(3):
    print(name)

#Challenge 36
print('Challenge 36\n\n')

name=input('Enter your name.\n')
num=int(input('Enter a number.\n'))
print('\n\n')
for i in range(num):
    print(name)

#Challenge 37
print('Challenge 37\n')

name=input('Enter your name.\n')
for x in name:
    print(x)

#Challenge 38
print('Challenge 38\n')

name=input('Enter your name.\n')
num=int(input('Enter a number\n'))
for num in range(num):
    for x in name:
        print(x)

#Challenge 39
print('Challenge 39\n')

num=int(input('Enter a number between 1 and 12\n'))
count=0
print(f'The times tables of {num} are;')
for i in range(1,13):
    print(f'{i} x {num} = {i*num}')

#Challenge 40
print('Challenge 40\n')

num=int(input('Give me a number below 50'))
fifty=50
print(50)
while True:
    print(fifty-1)
    fifty-=1
    if fifty == num:
        break
print(fifty)

#Challenge 41
print('Challenge 41\n')

name=input('Enter your name.\n')
num=int(input('Enter a number.\n'))
print('\n')
if num < 10:
    for i in range(num):
        print(name)
else:
    for i in range(3):
        print('Too high.')

#Challenge 42
print('Challenge 42\n')

total=(0)
for i in range(5):
    num=int(input('Enter a number.\n'))
    yesno=input('Do you want to add this number to the total?')
    if 'yes' in yesno:
        total+=num
print(f'Your total is {total}.')

#Challenge 43
print('Challenge 43\n')


direction=input('Which direction do you want to count in? (up or down)\n')
if 'up' in direction:
    _=0
    num=int(input('Give me the top number.\n'))
    while True:
        print(_+1)
        _+=1
        if _ == num:
             break
elif 'down' in direction:
    _=20
    num=int(input('Enter a number below 20.\n'))
    while True:
        print(_-1)
        _-=1
        if _ == num:
            break

#Challenge 44
print('Challenge 44\n')

num=int(input('How many people do you want to invite to a party?\n'))
if num < 10:
    for i in range(num):
        name=input(f'Enter in the name of person {i}:')
        print(f'{name} has been invited.\n')
else:
    print('Too many people.')