commandTable = {
    #Add: Get Top, Decrement SP, Get Top, Add, Store
    'add' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D+M \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'sub' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=M-D \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'and' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D&M \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'or' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D|M \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'not' : '@SP\nM=M-1\nA=M \nM=!M\n@SP\nM=M+1\n',
    'neg' : '@SP\nM=M-1\nA=M \nM=-M\n@SP\nM=M+1\n',
}

# Push Abstraction for Stack Arithmetic
def push( segment, value):
    if not segment == 'constant' :
        return
    str = '@'+value+'\nD=A\n' # D = value 
    str += '@SP\nA=M\n' # A now at stack pointer position
    str += 'M=D\n' # Store data at new location 
    str += '@SP\nM=M+1\n' # Increment stack pointer
    return str

# Pop Abstraction
def pop( segment , value):
    return

