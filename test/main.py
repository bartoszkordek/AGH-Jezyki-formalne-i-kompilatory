import os
import sys
import getopt
from mylexer import lexer
from myparser import parser


def compile(input_file_name, output_file_name):
    current_folder_path = os.path.dirname(__file__)
    input_file_name = input_file_name + ".txt"
    output_file_name = output_file_name+".txt"
    folder_input = "\\input\\"
    folder_output = "\\output\\"

    input_file = open(current_folder_path +
                      folder_input + input_file_name, "r")

    result = parser.parse(input_file.read())

    output_file = open(current_folder_path +
                       folder_output + output_file_name, "w")
    output_file.write(str(result))

    print("Done!")


def main(argv):
    input_file = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(
            argv, "hi:o:", ["inputfile=", "outputfile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            input_file = arg
        elif opt in ("-o", "--outputfile"):
            output_file = arg
        else:
            print('Invalid command')
            print('Type for help: python test.py -h')
            sys.exit()

    compile(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
