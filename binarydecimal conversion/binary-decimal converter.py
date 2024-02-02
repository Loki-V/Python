import library

print("----------Binary/Decimal Converter----------")
x = input("\n\n1.Binary to Decimal\n2.Decimal to Binary\n3.Add two Binary numbers.\n4.Hexadecimal to binary\n5.Binary to Hexadecimal\nEnter the number to select: ")

if x == '1':
    bi = int(input("Enter your Binary number: "))
    print(f"Your Decimal number is:{library.BD(bi)}")
    


if x == '2':
    dec = int(input("Enter your decimal number: "))
    print(f"Your Binary number is:{library.DB(dec)}")
    
if x == '3':
    binary1 = int(input("Enter first binary number."))
    binary2 = int(input("Enter second binary number."))
    library.add(binary1,binary2)
    
if x == '4':
    hex = input('Enter your Hexadecimal number: ')
    _ = library.hexatobinary(hex)
    print(f"Your Binary number is:{library.DB(_)}")
    
if x == '5':
    dec = int(input("Enter your binary number: "))
    _ = library.BD(dec)
    print(f"Your Hexadecimal is:{library.bintohex(_)}")
    
