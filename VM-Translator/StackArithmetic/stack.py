commandTable = {
    #Add: Get Top, Decrement SP, Get Top, Add, Store
    'add' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D+M \n@SP\nA=M\nM=D \n@SP\nM=M+1',
    'sub' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D-M \n@SP\nA=M\nM=D \n@SP\nM=M+1',
    'and' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D&M \n@SP\nA=M\nM=D \n@SP\nM=M+1',
    'or' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D|M \n@SP\nA=M\nM=D \n@SP\nM=M+1',
}
#Eq = sub == 0?
#get and lt
#not , neg


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
def pop( segment ):
    return

