commandTable = {
    #Add: Get Top, Decrement SP, Get Top, Add, Store
    'add' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D+M \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'sub' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=M-D \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'and' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D&M \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'or' : '@SP\nM=M-1\nA=M\nD=M \n@SP\nM=M-1\nA=M \nD=D|M \n@SP\nA=M\nM=D \n@SP\nM=M+1\n',
    'not' : '@SP\nM=M-1\nA=M \nM=!M\n@SP\nM=M+1\n',
    'neg' : '@SP\nM=M-1\nA=M \nM=-M\n@SP\nM=M+1\n',
}
segment_symbol = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
    "static": 16,
    "temp": 5
}

def get_base_address(segment, index="0"):
    if segment == 'constant':
        return index
    elif segment == 'pointer':
        return segment_symbol['this'] if index == "0" else segment_symbol['that']
    elif segment in ['static', 'temp']:
        return str(int(segment_symbol[segment]) + int(index))
    else:
        return segment_symbol[segment]

# Push Abstraction for Stack Arithmetic
def push( segment, value, filename=''):
    if segment == 'constant':
        set_data = "D=A\n"
    elif segment in ['pointer', 'static', 'temp']:
        set_data = "D=M\n"
    else:
        set_data = "D=M\n"
        set_data += "@%s\n" % value
        set_data += "A=D+A\nD=M\n"
    
    str = "@%s\n" % (get_base_address(segment, value) if segment != 'static' else filename+"."+value)
    str += set_data
    str +=  "@SP\nM=M+1\nA=M-1\nM=D\n"
    return str

# Pop Abstraction
def pop( segment , value, filename = ''):
    error = True

    # Constant pop error
    if segment == 'constant':
        return '',error
    elif segment in ['pointer', 'temp' , 'static']:
        str = '@SP\nAM=M-1\nD=M\n'
        str += "%s\n" % get_base_address(segment,value) if segment != 'static' else filename+"."+value
        str += 'M=D\n'
        return str , not(error)
    else :
        str = '@%s\n' % get_base_address(segment)
        str += 'D=M\n'
        str +=  '@%s\n' % value
        str += 'D=D+A\n@15\nM=D\n@SP\nAM=M-1\nD=M\n@15\nA=M\nM=D\n'
        return str , not(error)
