load CS16B021AddSub16.hdl,
output-file CS16B021AddSub16.out,
output-list a%B1.16.1 b%B1.16.1 sel%B1.1.1 out%B1.16.1;

set a %B0000000000000000,
set b %B0000000000000000,
set sel 0,
eval,
output;
set sel 1,
eval,
output;



set a %B0000000000000000,
set b %B1111111111111111,
set sel 0,
eval,
output;
set sel 1,
eval,
output;

set a %B1111111111111111,
set b %B1111111111111111,
set sel 0,
eval,
output;
set sel 1,
eval,
output;

set a %B1010101010101010,
set b %B0101010101010101,
set sel 0,
eval,
output;
set sel 1,
eval,
output;

set a %B0011110011000011,
set b %B0000111111110000,
set sel 0,
eval,
output;
set sel 1,
eval,
output;

set a %B0001001000110100,
set b %B1001100001110110,
set sel 0,
eval,
output;
set sel 1,
eval,
output;
