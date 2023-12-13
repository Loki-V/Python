#Hangman
import check
import time
import random
import nooselevels
import images
score = 0
lives = 10
guesses = []
letter = 0

nooselevels.logo()
name = input("Enter your name: ")
hard = ["assassin","butcher","executive","executioner","quip","huge","foyer","ornithology","zooology","xylophone","zebra","uwe"]
x = random.choice(hard)
normal = ["apple","earbud","dogwater","ultrakill","pissbot","dingleberry","balls","licking","bingo"]
y = random.choice(normal)
easy = ["ingot","three","a","or","it"]
z = random.choice(easy)

difficulty = input('\nChoose a difficulty:\neasy\nnormal\nhard\n')
if difficulty == 'easy':
    word = z.upper()
if difficulty == 'normal':
    word = y.upper()
if difficulty == 'hard':
    word = x.upper()

ans = "_" * len(word)
ans = list(ans)



time.sleep(.3)
print(f"\nWelcome {name}.\n\n\n\n\n\n\n")
time.sleep(1.2)
nooselevels.start()
print(f"The word is:{' '.join(ans)}\n\n\n\n")

check.check(lives,score,word,ans,guesses)

if lives > 0:
        
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠴⠒⠢⠤⠄⣀')
    print('⠀⠀⠀⠀⠀⠀⣠⠔⠉⣥⣤⣤⣤⠀⠀⢀⣤⣬⣵⠦⡀')
    print('⠀⠠⢤⡴⣐⡼⠁⠀⠀⠉⠉⠉⠀⠀⠀⠀⠈⠉⠉⠀⠉⢆')
    print('⠀⡗⢺⢬⣋⣍⣲⣄⣠⣴⣴⣶⣦⣄⣀⣀⣠⣴⣶⣶⣤⣌⣦')
    print(' ⡝⠩⣾⠯⡽⣹⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⡄')
    print('⢸⠁⢸⣫⡀⠽⠉⠈⢿⣿⣿⣿⣿⣿⡏⢿⣿⣿⣿⣿⡿⠃⢸')
    print('⠘⠣⠟⢻⡀⠀⢠⢤⣤⣉⣻⣟⣋⣁⣀⣀⣉⣉⣭⡿⠗⠀⡸⠀⠀⠤⡀')
    print('⠀⠀⠀⠈⣷⠀⠀⠀⠈⠻⣶⠤⢼⠤⡗⠐⡗⣟⠟⠁⠀⢠⠇⠀⠀⢸⢒⡇')
    print('⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⢤⡁⠘⠒⠒⠒⢋⡡⠖⠀⣠⠎⠀⠀⠀⣼⣷⠓⠒⠄')
    print('⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠉⠐⠒⠒⠂⠉⠀⣠⠞⠁⠀⠀⠀⢸⣿⣏⠒⠒⢦')
    print('⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⠶⠤⠤⠤⠤⠴⠒⠉⠀⠀⠀⠀⠀⠀⠀⠹⣏⠁⢰⡉')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠈⠉⠉')

yesno = input("\n\nDo you want to try again? Y/N\n")
if yesno != 'Y' and yesno != 'y':
     exit()

while True:
    score = 0
    lives = 10
    guesses = []
    letter = 0

    nooselevels.logo()
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome back {name}!")
    hard = ["assassin","butcher","executive","executioner","quip","huge","foyer","ornithology","zooology","xylophone","zebra","uwe"]
    x = random.choice(hard)
    normal = ["apple","earbud","dogwater","ultrakill","pissbot","dingleberry","balls","licking","bingo"]
    y = random.choice(normal)
    easy = ["ingot","three","a","or","it"]
    z = random.choice(easy)

    difficulty = input('\nChoose a difficulty:\neasy\nnormal\nhard\n')
    if difficulty == 'easy':
        word = z.upper()
    if difficulty == 'normal':
        word = y.upper() 
    if difficulty == 'hard':
        word = x.upper()

    ans = "_" * len(word)
    ans = list(ans)



    time.sleep(.3)
    print(f"Game start\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1.2)
    nooselevels.start()
    print(f"The word is:{' '.join(ans)}\n\n\n\n")

    check.check(lives,score,word,ans,guesses)

    if lives > 0:
            
        print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠴⠒⠢⠤⠄⣀')
        print('⠀⠀⠀⠀⠀⠀⣠⠔⠉⣥⣤⣤⣤⠀⠀⢀⣤⣬⣵⠦⡀')
        print('⠀⠠⢤⡴⣐⡼⠁⠀⠀⠉⠉⠉⠀⠀⠀⠀⠈⠉⠉⠀⠉⢆')
        print('⠀⡗⢺⢬⣋⣍⣲⣄⣠⣴⣴⣶⣦⣄⣀⣀⣠⣴⣶⣶⣤⣌⣦')
        print(' ⡝⠩⣾⠯⡽⣹⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⡄')
        print('⢸⠁⢸⣫⡀⠽⠉⠈⢿⣿⣿⣿⣿⣿⡏⢿⣿⣿⣿⣿⡿⠃⢸')
        print('⠘⠣⠟⢻⡀⠀⢠⢤⣤⣉⣻⣟⣋⣁⣀⣀⣉⣉⣭⡿⠗⠀⡸⠀⠀⠤⡀')
        print('⠀⠀⠀⠈⣷⠀⠀⠀⠈⠻⣶⠤⢼⠤⡗⠐⡗⣟⠟⠁⠀⢠⠇⠀⠀⢸⢒⡇')
        print('⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⢤⡁⠘⠒⠒⠒⢋⡡⠖⠀⣠⠎⠀⠀⠀⣼⣷⠓⠒⠄')
        print('⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠉⠐⠒⠒⠂⠉⠀⣠⠞⠁⠀⠀⠀⢸⣿⣏⠒⠒⢦')
        print('⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⠶⠤⠤⠤⠤⠴⠒⠉⠀⠀⠀⠀⠀⠀⠀⠹⣏⠁⢰⡉')
        print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠉⠉')

    yesno = input("\n\nDo you want to try again? Y/N\n")
    if yesno != 'y' and yesno != 'Y':
        break

print("Closing Game.")
exit()






     
        
        














