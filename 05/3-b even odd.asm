//comment
@13
(LOOP)
	//Store A
	D=A
	//Unit digit and 
	M=M&1
	A=M 
	//A = 0 if even, 1 if odd
	M=M+1
	A=D-1
	@END	
	A;JEQ
	@LOOP
	0;JMP
(END)
	@END
	0;JMP
