import sys 
import re

def replaceLabels(assemblycode):
    newcode = []
    labelTable = dict()
    labelpattern = re.compile(r"^\(\w*\)$")
    linenum = 0
    asmlinenum = 0
    for line in assemblycode:

        line=line.replace(' ','')
        line=line.replace('\n','')

        #Labelmatch
        if labelpattern.match(line):
            label = line[1:][:-1]
            labelTable[label] = linenum
        else:    
            #Normal code
            # Remove comment
            line = line.split("//")[0]
            if not line :
                print (end = "\n")
                continue
            #A instr with labels
            
            if line[0] == '@' and (not line[1:].isdigit()):    
                #Fetch if in table
                if labelTable.get(line[1:]) :
                    newcode.append('@'+str(labelTable.get(line[1:]))+'\n')
                    linenum += 1
                    continue
                else:
                    print (line , " => Label not found at line number ", asmlinenum, end="\n")
                    return ' ', True
            newcode.append(line)
            linenum += 1 
        asmlinenum += 1    
    return newcode, False

#Codes
compTable = {
    '0':'101010', '1':'111111', '-1':"111010", 'D':'001100', 'A':'110000', 
    'M':'110000', '!D':'001101', '!A':'110001','!M':'110001', '-D':'001111', 
    '-A':'110011', '-M':'110011', 'D+1':'011111', 'A+1':'110111', 'M+1':'110111', 
    'D-1':'001110', 'A-1':'110010','M-1':'110010', 
    'D+A':'000010', 'A+D':'000010',
    'D+M':'000010', 'M+D':'000010',
    'D-A':'000010', 
    'D-M':'000010', 
    'A-D':'000111',
    'M-D':'000111',
    'D&A':'000000', 'A&D':'000000',
    'D&M':'000000', 'M&D':'000000',
    'D|A':'010101', 'A|D':'010101',
    'D|M':'010101', 'M|D':'010101'}
jumpTable = {'null':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

def checkComp(comp):
    if comp in ["0","1","-1","D","A","!D","!A","-D","-A","D+1","A+1","D-1","A-1","D-A","A-D","M","!M","-M","M+1","M-1","D-M","M-D","A+D","D+A","A|D","D|A","D&A","A&D","M+D","D+M","D&M","M&D",]: 
        return True
    return False
def checkJump(jump):
    if jump in ['null','JGT','JEQ','JGE','JLT','JNE','JLE','JMP']:
        return True
    return False
def checkDest(dest):
    if dest in ["null","A","M","D","AM","AD","MD","AMD"]:
        return True   
    return False
# dest code
def getdest(dest):
    if dest == 'null':
        return '000'
    code = ''
    for i in 'ADM':
        if i in dest:
            code += '1'
        else:
            code += '0'
    return code

# returns C instruction
def generateCinstr(dest,comp,jump):
    error = False
    instr = '111'
    if 'M' in comp:
        instr += '1'
    else:
        instr += '0'
    
    if not (checkComp(comp) and checkJump(jump) and checkDest(dest)):
        error = True
        return ' ', error
    instr += compTable[comp]
    instr += getdest(dest)
    instr += jumpTable[jump]    
    return instr , error

# DEST = COMP ; JUMP
def printCinstr(line):
    llist = []

    # If dest exists
    if '=' in line:
        temp1 = line.split('=',1)
        llist.append(temp1[0]) #Get DEST 
        
        #if jump exists
        if ';' in temp1[1]:
            temp2 = temp1[1].split(';')
            llist.append(temp2[0]) #Get Compt
            llist.append(temp2[1]) #Get JUMP
            print (llist)
            #return getCInstr(llist)
        else:
            llist.append(temp1[1]) #Get Comp
            llist.append('null') #No JUMP
    else:
        llist.append('null') #No DEST
        
        #if jump exists
        if ';' in line:
            temp2 = line.split(';')
            llist.append(temp2[0]) #Get Compt
            llist.append(temp2[1]) #Get JUMP
            #return getCInstr(llist)
        else:
            llist.append(temp1[1]) #Get Comp
            llist.append('null') #No JUMP
            
    #print (llist)    
    instr,error = generateCinstr(llist[0],llist[1],llist[2])
    return instr,error

# Execution begins
argumentList = sys.argv
fname = sys.argv[1].rstrip()

#Check if name is right
x = re.findall(".asm$", fname)
if len(x)==0:
    print ("Incorrect file name")

#Open asm file
asmfile = open(fname, "r")
codelines = asmfile.readlines()
newcode,err = replaceLabels(codelines)
if err :
    asmfile.close()
    exit()
    
hackfile = open(fname.replace('.asm','.hack'),"a+")

#Read line by line
for line in newcode:
  line=line.replace(' ','')
  line=line.replace('\n','')
  print(line,' => ',end = '') 
  
  if line[0]== '@':
    # Converting numbers from integer to binary
    code = '0{0:015b}'.format(int(line[1:]))
  else :
    code, error = printCinstr(line)
    if error:
        print("Error : Wrong Instruction")
        break      
  print(code, end = "\n")
  hackfile.write(code+"\n")

print ( "Conversion successful. ")
asmfile.close()
hackfile.close()

