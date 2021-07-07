#!/usr/bin/python3
"""
    A simple python script that converts LEGv8 Instruction code into Machine Code. Done for ELET3405
"""

def main():
    '''
        Formats supported: R, I, D
        R: Opcode(11b), Rm(5b), shamt(6b), Rn(5b), Rd(5b)
        I: Opcode(10b), Immediate(12b), Rn(5b), Rd(5b)
        D: Opcode(11b), Address(9b), Op2(2b), Rn(5b), Rt(5b)

    '''
    Inst_Formats = {
            'ADD': { 'type': 'R', 'code': '10001011000'},
            'SUB': { 'type': 'R', 'code': '11001011000'},
            'AND': { 'type': 'R', 'code': '10001010000'},
            'ORR': { 'type': 'R', 'code': '10101010000'},
            'LDUR': { 'type': 'D', 'code': '11111000010'},
            'STUR': { 'type': 'D', 'code': '11111000000'},
            'ADDI': { 'type': 'I', 'code': '1001000100'},
            'SUBI': { 'type': 'I', 'code': '1101000100'}
    }

    input_file = input("Input file name: ")
    output_file = input("Output file name: ")
    print("The input file is: \'" + input_file + "\' and the output file is: \'" + output_file + "\'.")
    # Open file. Add try catch if file doesn't exist
    inf = open(input_file,"r")
    outf = open(output_file,"w")

    lines = inf.readlines()

    binaryCode = ''
    count = 0
    for line in lines:
        count += 1
        tmp = line.replace(',', '') #Remove all comma's to make splitting easier
        tmp = tmp.replace('[', '') #Remove ['s
        tmp = tmp.replace(']', '') #Remove ]'s
        tmp = tmp.replace('X', '') #Remove all X's
        tmp = tmp.replace('#', '') #Remove all #'s
        tmp = tmp.split(' ') # Separate commands by space
        
        # Currently some bugs in the evaluations
        #Check for instruction type format. Go into branches
        if Inst_Formats[tmp[0]]['type'] == 'R': # R format
            binaryCode += Inst_Formats[tmp[0]]['code'] # opcode
            binaryCode += bin(int(tmp[3]))[2:].zfill(5) # Rm
            binaryCode += '000000' # shamt (6 0 bits for this project)
            binaryCode += bin(int(tmp[2]))[2:0].zfill(5) # Rn
            binaryCode += bin(int(tmp[1]))[2:0].zfill(5) # Rd
        elif Inst_Formats[tmp[0]]['type'] == 'D': # D format
            binaryCode += Inst_Formats[tmp[0]]['code'] # opcode
            binaryCode += bin(int(tmp[3]))[2:].zfill(9) # address
            binaryCode += '00' # op2 (They're both just 00 for LDUR and STUR)
            binaryCode += bin(int(tmp[2]))[2:].zfill(5) # Rn
            binaryCode += bin(int(tmp[1]))[2:].zfill(5) # Rt
        elif Inst_Formats[tmp[0]]['type'] == 'I': # I format
            binaryCode += Inst_Formats[tmp[0]]['code'] # opcode
            binaryCode += bin(int(tmp[3]))[2:0].zfill(12) # immediate
            binaryCode += bin(int(tmp[2]))[2:0].zfill(5) # Rn
            binaryCode += bin(int(tmp[1]))[2:0].zfill(5) # Rd
        else:
            print('Instruction: ' + tmp[0] + ' not found.. exiting')
            return 1

        hexcode = hex(int(binaryCode, 2))
        outf.write(line.rstrip() + " " + binaryCode +  " " + hexcode + "\n")

if __name__ == "__main__":
    main()
