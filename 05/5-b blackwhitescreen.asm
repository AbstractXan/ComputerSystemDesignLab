@43690 // 1010101010101010
D=A
@0
M=D

@21845 // 0101010101010101
D=A
@1
M=D

@SCREEN
D=A
@16383 //Store temp value for pointer
M=D


(LOOP) // 31 times loop then switch

@0 // 1010101010101010
D=M

@16383
A=M // Retrieve pointer
M=D // Assign value

@16383
M=M+1 

@LOOP
0;JMP


