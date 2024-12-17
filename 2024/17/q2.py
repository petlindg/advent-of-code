from numpy import bitwise_xor as bxor
import re
def getCombo(registers, op):
    if op == 4:
        return registers[0]
    elif op == 5:
        return registers[1]
    elif op == 6:
        return registers[2]
    elif op == 7:
        raise RuntimeError("Invalid operand")
    else:
        return op
def execOp(registers, program, pc, output):
    op = program[pc]
    l = program[pc+1]
    c = getCombo(registers, l)
    pc += 2
    if op == 0:
        registers[0] = int(registers[0]/(2**c))
    elif op == 1:
        registers[1] = bxor(registers[1], l)
    elif op == 2:
        registers[1] = c%8
    elif op == 3:
        if registers[0]!=0:
            pc = l
    elif op == 4:
        registers[1] = bxor(registers[1], registers[2])
    elif op == 5:
        output.append(c%8)
    elif op == 6:
        registers[1] = int(registers[0]/(2**c))
    elif op == 7:
        registers[2] = int(registers[0]/(2**c))
    return pc

f = open("input.txt", "r").read().split("\n\n")
registers = list(map(int, re.findall("[0-9]+",f[0])))
program = list(map(int, re.sub("Program: ", "", f[1]).split(',')))

acs = [(0, 0)]
c = 0
solutions = []
while len(acs)>0:
    (c, ac) = acs.pop()
    ac<<=3
    i = len(program)-c-1
    a = 0
    for a in range(8):
        registers[0] = ac|a
        pc = 0
        output = []
        while pc < len(program):
            pc = execOp(registers, program, pc, output)
        if output[0:c] == program[i:i+c]:
            acs.append((c+1, ac|a))
        if output == program:
            solutions.append(ac|a)

print(solutions)
print(acs)
for ac in solutions:
    registers[0]=ac
    pc=0
    output=[]
    while pc < len(program):
        pc = execOp(registers, program, pc, output)
    print(ac)
    print(program)
    print(output)
print(min(solutions))