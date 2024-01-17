import library

print("----------Binary/Decimal Converter----------")
x = input("\n\n1.Decimal to Binary\n2.Binary to decimal\nenter '1' or '2' to select: ")

if x == '1':
    bi = int(input("Enter your binary number: "))
    library.BD(bi)


if x == '2':
    dec = int(input("Enter your decimal number: "))
    library.DB(dec)
