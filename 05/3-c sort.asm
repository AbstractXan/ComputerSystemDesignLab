// Assume the array is of fixed length 10 i.e 0-9
// Array numbers are stored from 0-9

//Start from beginning
@10 //Store pointer at 10
D=0
M=D

@11
M=D
(LOOP)
	// for pointer position
	@10
	A=M
	
	// Find whether 1
	D=1
	D=M&D
	
	@INC
	D;JGT //JUMP to D when 1
	
	(CONT) // Otherwise it's okay, continue
	
	//Increment pointer
	@10
	M=M+1
	D=M
	
	@9 // A = 9
	D=A // D = 9
	@10
	D=D-M // D = D - next address
	
	@LOOP // Loop until reach 9
	D;JGE
	
	@SORT // Out of loop? Sort
	0;JMP
	
(INC)
	@11 // Store number of 1s in 11
	M=M+1
	@CONT
	0;JMP

(SORT)
	
	// If number of 1s is 0, end
	@11
	D=M	
	@END
	D;JLE	
	
	@10 //Start from 0
	D=0
	M=D
	(ONES) // Input ones

		//Decrement number of 1s
		@11
		M=M-1
		D=M
		
		@ZERO // Print zeroes if number of ones are over
		D;JLT
		
		//Otherwise continue
		@10
		A=M
		M=1 //Change to 1
		
		@10 // Increment pointer
		M=M+1
	
		@ONES // Loop until 1s are zero
		0;JGE
		
	(ZERO)
		@9 // A = 9
		D=A // D = 9
		@10
		D=D-M // D = D - next address
	
		@END // Loop until reach 9
		D;JLE
		
		@10 //Goto pointer
		A=M
		M=0 // Make value 0
		
		@10 // Increment Pointer
		M=M+1
		
		@ZERO// Keep looping
		0;JMP
	
	
(END)
	@END
	0;JMP
	

