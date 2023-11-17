#Subprograms

def sub1(A,B,C):
    print('------------------------------------------------------------------------------')
    print('This program will take the three numbers you give it and tell you the highest one.')
    print('------------------------------------------------------------------------------')

    if A > B and (A > C):
        response = A
    elif B > A and (B > C):
        response = B
    else:
        response = C
    return response

def sub2(A,B,C):
    print('------------------------------------------------------------------------------')
    print('This program will take the three numbers you give it and tell you the highest one.')
    print('------------------------------------------------------------------------------')
    
    if A > B:
        if A > C:
            print(A)
        else:
            ans = A
    else:
        if B>C:
            ans = B
        else:
            ans = C
    return ans

def sub3(A,B,C):
    print('------------------------------------------------------------------------------')
    print('This program will take the three numbers you give it and tell you the highest one.')
    print('------------------------------------------------------------------------------')

    maximum = A
    if maximum < B:
        maximum = B
    if maximum < C:
        maximum = C
    return maximum
