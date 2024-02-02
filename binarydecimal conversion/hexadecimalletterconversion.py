#Hexadecimal letter conversion

def letter(x):
    A = '10'
    B = '11'
    C = '12'
    D = '13'
    E = '14'
    F = '15'
    
    if x == 'A':
        x =  A
    if x == 'B':
        x =  B
    if x == 'C':
        x =  C
    if x == 'D':
        x =  D
    if x == 'E':
        x =  E
    if x == 'F':
        x =  F
    return x

def number(x):
    if x == 10:
        x =  'A'
    if x == 11:
        x =  'B'
    if x == 12:
        x =  'C'
    if x == 13:
        x =  'D'
    if x == 14:
        x =  'E'
    if x == 16:
        x =  'F'
    return x