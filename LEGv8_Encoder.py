#!/usr/bin/python3

# todo: add instruction functions

def main():
    input_file = input("Input file name: ")
    output_file = input("Output file name: ")
    print("The input file is: \'" + input_file + "\' and the output file is: \'" + output_file + "\'.")
    # Open file. Add try catch if file doesn't exist
    #inf = open( ,"r")
    outf = open( ,"w")

    lines = inf.readlines()

    count = 0
    for line in lines:
        count += 1
        tmp = line.replace(',', '') #Remove all comma's to make splitting easier
        # Check if there are []'s
        tmp = line.split(' ') # Separate commands by space

        
        outf.write(line + " " + binaryCode +  " " + hexcode)

if __name__ == "__main__":
    main()
