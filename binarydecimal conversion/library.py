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
    
def add(binary1,binary2):
       
    store = 0
    _ = 0
    y = 0
    ans = []
    n1 = str(binary1)[::-1]
    n2 = str(binary2)[::-1]
    num1 = list(n1)
    num2 = list(n2)
    num2.append('0')
    num1.append('0')
    if len(n1) < len(n2):
        num1.append('0')
        num1.append('0')
    if len(n2) < len(n1):
        num2.append('0')
        num2.append('0')
        
    num1 = str(num1)
    num1 = num1.replace(']','')
    num1 = num1.replace('[','')
    num1 = num1.replace(' ','')
    num1 = num1.replace(',','')
    num1 = num1.replace('"','')
    num1 = num1.replace("'","")

    num2 = str(num2)
    num2 = num2.replace(']','')
    num2 = num2.replace('[','')
    num2 = num2.replace(',','')
    num2 = num2.replace(' ','')
    num2 = num2.replace('"','')
    num2 = num2.replace("'","")

    while _ <= len(n1) and _ <= len(n2):
        y = int(num1[_])+int(num2[_])+store
        store = 0
        if y == 2:
            y = 0
            store = 1
        elif y == 3:
            y = 1
            store = 1
        ans.insert(0,y)
        _ += 1

    ans = str(ans)
    ans = ans.replace(',','')
    ans = ans.replace(' ','')
    ans = ans.replace('[','')
    ans = ans.replace(']','')
    print(ans) 


