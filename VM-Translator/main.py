import sys
import os
import re
import stack

operators = ['add','sub','neg','eq','gt','lt','and','or','not']
memoryOperators = ['push','pop']
memorySegments = { 
    'static':'SP','local':'LCL','this':'THIS',
    'that':'THAT','argument':'ARG','temp':'TMP'
    }
branchingCommands = ['label','goto','if-goto'] #!!!
functionCommands = ['function','call','return']
commandPattern = re.compile(r"(\w+)( \w+ \w+)?( )?") #Matching input with \w \w \w or \w

def translateLine(tokens):
    command = tokens[0]
    seg = tokens[1]
    if (command in memoryOperators) :
        if command == 'push':
            return stack.push(seg,tokens[2])
    return
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

hackfile = open(fname.replace('.vm','.asm'),"a+")

#Read line by line
for line in codelines:
  line=line.replace('\n','')
  print(line,' => ',end = '') 
  
  #Parse lines
  if not commandPattern.match(line):
    print("Error : Wrong Instruction")
    break 

  tokens = line.split(' ')
  assemblycode, error = translateLine(tokens)
  if error:
    print("Error : Wrong Instruction")
    break  
  hackfile.write(assemblycode+'\n')

print ( "Conversion successful. ")
asmfile.close()
hackfile.close()