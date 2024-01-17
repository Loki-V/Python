#binary/decimal converter functions


def BD(binary):
    x = 1
    y = 0
    for i in str(binary)[::-1]:
        y+= int(i)*x
        x = x*2
    print(f"Your Binary number is: {y}") 


def DB(decimal):
    binary = []
    x = decimal

    while True:
        r = x % 2
        x = x // 2
        binary.insert(0,r)
        if x == 1:
            binary.insert(0,x)
            break
    ans = str(binary)
    ans = ans.replace(',','')
    ans = ans.replace(' ','')
    ans = ans.replace('[','')
    ans = ans.replace(']','')
    print(f"The decimal number {decimal} is {ans} in binary.")
        
            
    
