#User Account Program

FirstLine = (f"User ID, Password\n")
Psswd = open("C:/Users/20LWehder.ACC/Documents/Library/AccountData.csv",'r')

def AddPass():
    while True:
        print("\nPassword must include each of the following:\n1. It should have at least 8 characters\n2. It should include upper case and lower case letters\n3. It should include numbers\n4. It should include one of these special characters; !, £, $, €, &, %, *, #\n")
        Password = input("Enter your password: ")
        CheckPassword = input("Enter your password again: ")
        if Password != CheckPassword or PassCheck(Password) == False:
            print("\nPlease re-enter your password, enure your password follows guidelines.\n")
        else:
            break
    return Password


def changeFileMode(file, mode) :
    file.close()
    file = open(file.name, mode)
    return file

def PassCheck(Pass):
    symbol = ['!','£','$','€','&','*','#']
    check = False
    if len(Pass) >= 8:
        check = True
    else:
        check = False
    if Pass.isupper() == True or Pass.islower() == True:
        check = True
    else:
        check = False
    for i in Pass:
        if Pass.isdigit() == False and i in symbol:
            check = True
    return check
    

def AddID():
    while True:
        Psswd = open("C:/Users/20LWehder.ACC/Documents/Library/AccountData.csv",'r')
        NewID = input("\nInput new ID here: ")
        check = True
        for i in Psswd:
            line = i.split(',')
            if NewID not in line:
                check = False
            else:
                check = True
        if check == False:
            Psswd = changeFileMode(Psswd, 'a')
            Psswd.write(f"{NewID}, {AddPass()}\n")
            Psswd.close()
            break
        else:
            print("ID already exists, be more creative next time.")
        Psswd.close()

def CheckID():
    while True:
        Psswd = open("C:/Users/20LWehder.ACC/Documents/Library/AccountData.csv",'r')
        ID = input("\nInput your ID here: ")
        for i in Psswd:
            line = i.split(',')
            if ID in line[0]:
                del line[1]
                line.append(AddPass())
                Psswd.close()
                return ("Password changed successfully")
                
            else:
                continue
        print("\nID does not exist, make sure you enter the correct one.")
        
def IDPrint():
    Psswd = open("C:/Users/20LWehder.ACC/Documents/Library/AccountData.csv",'r')
    for i in Psswd:
        line = i.split(',')
        print(line[0])
    Psswd.close()



if FirstLine not in Psswd:
    Psswd = changeFileMode(Psswd, 'a')
    Psswd.write(FirstLine)
    Psswd.close()


while True:
    Menu = int(input("\n\n\n1)  Create a new user ID\n2)  Change a password\n3)  Display all user IDs\n4)  Quit\n"))
    match Menu:
        case 1:
            AddID()
            print("\nID added successfully\n\n\n\n")
        case 2:
            print(CheckID())
        case 3:
            IDPrint()
        case 4:
            Psswd.close()
            print("\nClosing\n")
            exit()

