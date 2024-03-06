#logic gates

def AndGate (x,y):
    if x =='1'and y =='1':
        return'1'
    else:
        return'0'

def OrGate (x,y):
    if x =='1'or y =='1':
        return'1'
    else: return'0'

def NotGate (x):
    if x =='1':
        return'0'
    else:
        return'1'
    
def NAndGate (x,y):
    if x =='1'and y =='1':
        return'0'
    else:
        return'1'
    
def NOrGate (x,y):
    if x =='0' and y =='0':
        return'1'
    else:
        return'0'
    
def XOrGate (x,y):
    if x =='1'and y =='0':
        return'1'
    if x =='0' and y =='1':
        return'1'
    else:
        return'0'
    
def XNOrGate (x,y):
    if x =='1'and y =='0':
        return'0'
    if x =='0' and y =='1':
        return'0'
    else:
        return'1'


    
    
    
    
    
    