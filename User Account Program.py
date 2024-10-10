#ID 1 = Loki   Pass: something
#ID 2 = bla    Pass: not something

space = ','
FirstLine = (f"User ID{space}Password\n")
Psswd = open("C:/Users/20LWehder.ACC/Documents/Library/AccountData.csv",'r')

Menu = int(input("1)  Create a new user ID\n2)  Change a password\n3)  Display all user IDs\n4)  Quit\n"))

def changeFileMode(file, mode) :
    file.close()
    file = open(file.name, mode)
    return file

def PassCheck(Pass):
    for i in Pass:
        if i.isdigit() is True:
            return True
        elif i == '!' or i == '£' or i == '$' or i == '€' or i == '&' or i == '%' or i == '*' or i == '#':
            return True
    if len(Pass) < 8:
        return False
    elif Pass.isupper() == True or Pass.islower() == True:
        return False
    else:
        return True
    

def AddID():
    while True:
        Psswd = open("C:/Users/20LWehder.ACC/Documents/Library/AccountData.csv",'r')
        NewID = input("\nInput new ID here: ")
        check = True
        for i in Psswd:
            line = i.split(space)
            if NewID not in line:
                check = False
            else:
                check = True
        if check == False:
            Psswd = changeFileMode(Psswd, 'a')
            while True:
                print("Password must include each of the following:\n1. It should have at least 8 characters\n2. It should include upper case and lower case letters\n3. It should include numbers\n4. It should include one of these special characters; !, £, $, €, &, %, *, #\n")
                NewPass = input("Enter your password: ")
                CheckPass = input("Enter your password again: ")
                if NewPass == CheckPass and PassCheck(NewPass) == True:
                    break
            Psswd.write(f"{NewID}{space}{NewPass}\n")
            Psswd.close()
            break
        else:
            print("ID already exists, be more creative next time.")
            Psswd.close()



if FirstLine not in Psswd:
    Psswd = changeFileMode(Psswd, 'a')
    Psswd.write(FirstLine)
    Psswd.close()


AddID()


Psswd.close()