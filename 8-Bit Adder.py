#8 Bit Adder

import LogicGates
import Adders

ans = []
x = []
y = []
num1 = input('Enter first 8-bit binary number: ')
num2 = input('\nEnter second 8-bit binary number')


#num1 = input("Enter first number: ")
#num2 = input("\nEnter second number: ")
carry = 0

for i in range(0,8):
    x.append(num1[i])
    y.append(num2[i])


for u in range(0,8):
    ans.append(Adders.FullAdder(x[u],y[u],carry)[0])
    carry = Adders.FullAdder(x[u],y[u],carry)[1]
    print(ans,sep='')
    str = ans
    ans = ans.remove


