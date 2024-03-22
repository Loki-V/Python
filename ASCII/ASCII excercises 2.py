import library

_ = list(input("Enter a phrase: "))
x = []
for i in _:
    x.append(library.DB(ord(i)))
print(x)


def byte4(x):
    x1 = '10' + x[-6::]
    x2 = '10' + x[-12:-6]
    if len(x) == 17:
        x3 = '100' + x[-17:-12]
    else:
        x3 = '10' + x[-18:-12]
    if len(x) == 19:
        x4 = '1111000' + x[-19:-18]
    elif len(x) == 20:
        x4 = '111100' + x[-20:-18]
    else:
        x4 = '11110' + x[:-18]
    ans = [x4,x3,x2,x1]
    str(ans)
    ans = ans.replace('[','')
    ans = ans.replace(']','')
    ans = ans.replace(',','')
    ans = ans.replace(' ','')
    ans = ans.replace(")",'')
    ans = ans.replace("(",'')
    ans = ans.replace("'",'')
    return ans


def byte3(x):
    x3 = ''
    x1 = '10' + x[-6::]
    if len(x) < 12:
        x2 = '100' + x[-12:-6]
    else:
        x2 = '10' + x[-12:-6]
    if len(x) >12:
        if len(x) == 13:
            x3 = '1110000' + x[1:-12]
        if len(x) == 14:
            x3 = '111000' + x[1:-12]
        if len(x) == 15:
            x3 = '11100' + x[1:-12]
        else:
            x3 = '1110' + x[1:-12]
    else:
        x3 = '1110000'
    ans = [x3,x2,x1]
    ans = str(ans)
    ans = ans.replace('[','')
    ans = ans.replace(")",'')
    ans = ans.replace("(",'')
    ans = ans.replace(']','')
    ans = ans.replace("'",'')
    ans = ans.replace(',','')
    ans = ans.replace(' ','')
    return ans

def byte2(x):
    x1 = x[-6::]
    x2 = x[0:-6]
    if len(x2) < 3:
        x2 = '000' + x2
    elif len(x2) < 4:
        x2 = '00' + x2
    elif len(x2) < 5:
        x2 = '0' + x2
    _1 = '10' + x1
    _2 = '110' + x2
    ans = (_2 , _1)
    ans = str(ans)
    ans = ans.replace('[','')
    ans = ans.replace(']','')
    ans = ans.replace(',','')
    ans = ans.replace(' ','')
    ans = ans.replace("'",'')
    ans = ans.replace(")",'')
    ans = ans.replace("(",'')
    return ans
    
    
def byte1(x):
    x1 = '0' + '0'*(7-len(x)) + x
    return x1

for i in x:
    if len(i) <= 7:
        print(byte1(i))
    elif len(i) <= 11:
        print(byte2(i))
    elif len(i) <= 16:
        print(byte3(i))
    elif len(i) <= 21:
        print(byte4(i))
    
