import sys
import os
import re
import stack

operators = ['add','sub','neg','and','or','not']
logicalOperators = ['gt','lt','eq']
operation_symbol = {
    "eq": "JNE",
    "gt": "JLE",
    "lt": "JGE"}
memoryOperators = ['push','pop']
branchingCommands = ['label','goto','if-goto'] #!!!
functionCommands = ['function','call','return']
commandPattern = re.compile(r"(\w+)( \w+ \w+)?( )?") #Matching input with \w \w \w or \w
counter = 0
filename = ''
# operators
def operatorHandler(operator):
    if stack.commandTable.get(operator):
        return stack.commandTable.get(operator)
    elif operator in logicalOperators:
        global counter
        str = ''
        for i in [
            '@SP\nAM=M-1\nD=M\n@13\nM=D', #Store top in Reg13
            '@SP\nAM=M-1\nD=M\n@15\nM=D', #Store top in Reg15
            "@13\nD=M\n","@14\nD=M-D",
            "@false%d" % counter,
            "D;%s" % operation_symbol[operator],
            "D=-1",
            "@set%d" % counter,
            "0;JMP",
            "(false%d)" % counter,
            "D=0",
            "(set%d)" % counter,
            #"@15\n",
            #"M=D\n", #Answer in Reg15
            '@SP\nA=M\nM=D']:
            str += i + '\n'
        counter += 1
        return str

# translateLine
def translateLine(tokens,filename=''):
    error = False
    # Push or Pop
    if (tokens[0] in memoryOperators) and (tokens[2].isdigit()) :
        if tokens[0] == 'push':
            return stack.push(tokens[1],tokens[2]) , error
        else:
            str , err = stack.pop(tokens[1],tokens[2]) 
            return str , (err or error)
    # Stack Arith
    elif (tokens[0] in operators) or (tokens[0] in logicalOperators):
        return operatorHandler(tokens[0]) , error
    elif tokens[0] == 'label':
        return '('+tokens[1]+')\n'
    elif tokens[0] == 'goto':
        return '@'+tokens[1]+'\n0;JMP\n'
    elif tokens[0] == 'if-goto':
        return '@SP\nAM=M-1\nD=M\n@'+tokens[1]+'\nD;JNE\n'
    
    return '', True

# Execution begins
argumentList = sys.argv
fname = sys.argv[1].rstrip()

#Check if name is right
x = re.findall(".vm$", fname)
if len(x)==0:
    print ("Incorrect file name")

#Open vm file
asmfile = open(fname, "r")
codelines = asmfile.readlines()

hackfile = open(fname.replace('.vm','.asm'),"w+")
filename = fname.replace('.asm','')
#Start
hackfile.write("@256\nD=A\n@SP\nM=D\n")

#Read line by line
for line in codelines:
  line=line.replace('\n','')
  print(line,' => ',end = '') 
  
  #Parse lines
  if not commandPattern.match(line):
    print("Error : Wrong Instruction")
    break 

  tokens = line.split(' ')
  assemblycode, error = translateLine(tokens,filename)
  if error:
    print("Error : Wrong Instruction")
    break  

  print(assemblycode,end='\n')
  hackfile.write(assemblycode)

print ( "Conversion successful. ")
asmfile.close()
hackfile.close()