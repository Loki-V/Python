#adders

import LogicGates

def FullAdder (x,y,z):
    if z != '1':
        z = '0'
    sum = LogicGates.XOrGate(LogicGates.XOrGate(x,y),z)
    carry = Logicgates.OrGate(LogicGates.AndGate(LogicGates.XOrGate(x,y),z),LogicGatesAndGate(x,y))
    return sum , carry
    
    
def HalfAdder (x,y):
    sum = LogicGates.XOrgate(x,y)
    carry = LogicGates.AndGate(x,y)
    return sum , carry