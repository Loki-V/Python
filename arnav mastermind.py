#megamind
import random

embededColorList = ["red", "green", "yellow", "brown", "cyan", "purple", "blue", "grey", "green", "pink", "violet", "maroon", "black", "white"]
probablity = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def GetRandomComputerColorList():
    return random.choices(embededColorList, probablity, k = 4)

    
def GetUserColorList():
    userString = input("enter four colors")
    list = userString.split()
    return list

def CompareColorList(UserColor,ComputerColor):
    correctCounter = 0
    misplacedColors = 0
    for i in range(4):
        if (UserColor[i] in ComputerColor):
            if (UserColor[i] == ComputerColor[i]):
                correctColors += 1
                continue
            misplacedColors += 1
        results = [correctCounter, misplacedColors]
        return results

def main():
    while True:
        results = CompareColorList(GetUserColorList(), GetRandomComputerColorList())
        if (results[0] == 4):
            print("you won")
            break
        print(f"Number of colors you got right: {results[0]} ")
        print(f"Number of misplaced Colors {results[1]} ")
            
main()