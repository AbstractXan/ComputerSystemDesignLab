// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/05/CPU.tst

load CPU.hdl,
output-file CPU.out,
compare-to CPU.cmp,
output-list time%S0.4.0 inM%D0.6.0 instruction%B0.16.0 reset%B2.1.2 outM%D1.6.0 writeM%B3.1.3 addressM%D0.5.0 pc%D0.5.0 DRegister[]%D1.6.1;

//@0
//M=1
//D=M

//@1
//M=D+1
//D=M

//@3
//M=D

//@0
//D=M
//@1
//M=D

//@3
//D=M
//@1
//M=D

//0000000000000000
//1110111111001000
//1111110000010000
//0000000000000001
//1110011111001000
//1111110000010000
//0000000000000011
//1110001100001000
//0000000000000000
//1111110000010000
//0000000000000001
//1110001100001000
//0000000000000011
//1111110000010000
//0000000000000001
//1110001100001000
