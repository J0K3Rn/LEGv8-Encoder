# LEGv8 Encoder
 
A simple python script that converts LEGv8 Instruction code into Machine Code.
Program will prompt user for an input file and output file separated by a space. The input file is presumed to have no errors.
	For Example:
		in.txt out.txt
The input file will contain LEGv8 Assembly code instructions.
The output file will contain the LEGv8 Assembly code instruction, it's binary representation and its hexidecimal value in that respective order.
	For Example:
        in.txt:
            ADD X9, X20, X21
            LDUR X2, [X20, #8]
        out.txt:
            ADD X9, X20, X21 10001011000101010000001010001001 0x8b150289
            LDUR X2, [X20, #8] 11111000010000001000001010000010 0xf8408282
    
To run: Simply execute the program with ./LEGv8_Encoder.py
Please provide the file extension when entering the input and output file.
