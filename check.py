#check
import images
import nooselevels
import time

def check(lives,score,word,ans,guesses):
    wordx = word
    while list(word) != ans:
        letter = input("Guess a letter: ")
        if letter.isalpha is False:
            letter = input("Guess a letter: ")
            
        else:
            letter = letter.upper()        
            if letter in wordx:
                x = wordx.count(letter)
                for i in range(0,x):
                    y = wordx.find(letter)
                    del ans[y]
                    ans.insert(y,letter)
                    wordx = list(wordx)
                    wordx.remove(letter)
                    wordx.insert(y,'-')
                    wordx = str(wordx)
                    wordx = wordx.replace("[","")
                    wordx = wordx.replace("]","")
                    wordx = wordx.replace("'","")
                    wordx = wordx.replace(",","")
                    wordx = wordx.replace(" ","")
                score += 1

            else:
                lives -=1
                guesses.append(letter)
            if lives == 0:
                nooselevels.dead()
                time.sleep(2)
                nooselevels.gameover()
                print(f"\n\nThe word is:{''.join(word)}\n\n")
                time.sleep(3)
                exit()

        print(images.image(lives))
        print(f"lives: {lives}")
        print(f"score: {score}")
        print(f"Incorrect Guesses: {', '.join(guesses)}\n")
        print(f"word is:{' '.join(ans)}")     
    return lives, score, ans, guesses
            
                
            
            
        
    