// Infinite program
//Store address at 2
@3
D=A
@2
M=D
//Begin at 3
@3
D=A
(LOOP)
	//and at unit's place
	A=D
	D=1
	D=M&D
	
	//update evens and odds
	A=D 
	M=M+1
	
	//retrieve address
	@2
	M=M+1
	D=M
	
	@LOOP
	0;JMP
