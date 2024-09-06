#Project Preparation
#1 2 3 55 5 0 7 8 9 124 11 12 12 14 12 3 3 18 19 20
import SimpleSort

#Mean
def Mean(UserList):
    Total = 0
    for i in range(len(UserList)-1):
        Total += UserList[i]
    Mean = Total / len(UserList)
    result = (f"\n\nMean: {Mean}")
    return result

#Median
def Median(UserList):
    if (len(UserList) % 2) == 0:
        x = len(UserList) / 2
        y = x+1
        Median = (x+y) / 2
    else:
        Median = UserList[len(UserList)%2]
    result = (f"Median: {Median}")
    return result

#Mode
def Mode(UseList):
    Mode = []
    x = 0
    for i in range(len(UserList)):
        y = UserList.count(UserList[i])
        if y > x:
            x = y
    for i in range(len(UserList)):
        if UserList.count(UserList[i]) == x and UserList[i] not in Mode:
            Mode.append(UserList[i])
    result = (f"The Mode/s:{Mode} occur {x} times in your list.")
    return result
    
#Frequency
def Frequency(UserList):
    Check = []
    for i in range(len(UserList)):
        if UserList[i] not in Check:
            Check.append(UserList[i])
            print(f"Frequency of value:{UserList[i]}= {UserList.count(UserList[i])}")

#Top 5 Numbers
def Top5(UserList):        
    result(f"Top 5 Numbers: {UserList[-5:]}")
    return result

#Last 5 Numbers
def Last5(Unsorted):
    result = (f"Last 5 Numbers: {Unsorted[-5:]}")
    return result




UserList = input("Enter values for List: ").split()

while len(UserList) > 20:
    print(f"\nYour list has {len(UserList)-20} too many values,\nplease reduce the amount of values in your list.")
    UserList = input("\nEnter values for new list: ").split()

UserList = list(map(int, UserList))
Unsorted = UserList.copy()
UserList = SimpleSort.Sort(UserList)

print("What would you like to do with your list?")
Choice = int(input("1.Mean\n2.Median\n3.Mode\n4.Frequency\n5.Top 5 numbers\n6.Last 5 numbers\n"))

match Choice:
    case 1:
        print(Mean(UserList))
    case 2:
        print(Median(UserList))
    case 3:
        print(Mode(UserList))
    case 4:
        print(Frequency(UserList))
    case 5:
        print(Top5(UserList))
    case 6:
        print(Last5(Unsorted))
