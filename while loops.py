#While loop exercises.


#Challenge 45
print('Challenge: 45\n')

total=0
while total <= 50:
    total+=int(input('Give me a number.\n'))
    print(f'The total is: {total}\n')
print(f'Finished, The total is over 50')

#Challenge 46
print('Challenge: 46\n')

num=0
while num<=5:
    num=int(input('Enter in a number.\n'))
print(f'The last number you entered was {num}.\n')
exit()


#Challenge 47
print('Challenge: 47\n')

yesno=''
num=int(input('Enter in a number.\n'))
num+=int(input('Enter in another number.\n'))
while True:
    yesno=input('Do you want to add another number?\ny/n\n')
    if 'y' in yesno:
        num+=int(input('Enter in your number.\n'))
    else:
        break
print(f'Total:{num}')

#Challenge 48
print('Challenge: 48\n')


name=input('Enter in the name of a person you would want to invite to a hypothetical party.\n')
print(f'{name} has been invited.')
count=1
while True:
    yesno=input('Do you want to invite someone else?\ny/n\n')
    if 'y' in yesno:
        name=input('Enter in the name of the next person invited.\n')
        count+=1
    elif 'n' in yesno:
        break
    else:
        print('ERROR\n')
        continue
print(f'There are {count} people coming to the party.')


#Challenge 49
print('Challenge: 49\n')

compnum=50
count=0
guess=int(input('Guess a number from 1 to 100.\n'))
while guess != compnum:
    guess=int(input('Guess again.\n'))
    count+=1
print(f'Well Done! You took {count} attempts.')


#Challenge 50
print('Challenge: 50\n')

while True:
    num=int(input('Enter a number between 10 and 20.\n'))
    if num > 20:
        print('Too High.')
    elif num < 10:
        print('Too low.')
    else:
        print('Thank You.')
        break

#Challenge 51
print('Challenge: 51\n')

bottles=10
while bottles != 0:
    num=int(input(f'There are {bottles} hanging on the wann, {bottles} hanging on the wall, and if 1 green bottle should accidentally fall.\n\nHow many bottles will be hanging on the wall?\n'))
    if num==bottles-1:
        bottles-=1
    else:
        print('No, try again.\n')
print('There are no more green bottles on the wall.')

    
        





