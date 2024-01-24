import library

print("----------Binary/Decimal Converter----------")
x = input("\n\n1.Decimal to Binary\n2.Binary to decimal\n3.Add two Binary numbers.\nenter the number to select: ")

if x == '1':
    bi = int(input("Enter your binary number: "))
    library.BD(bi)


if x == '2':
    dec = int(input("Enter your decimal number: "))
    library.DB(dec)
    
if x == '3':
    binary1 = int(input("Enter first binary number."))
    binary2 = int(input("Enter second binary number."))
    library.add(binary1,binary2)
