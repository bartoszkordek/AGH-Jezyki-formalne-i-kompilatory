import os
from mylexer import lexer
from myparser import parser

current_folder_path = os.path.dirname(__file__)
input_file_name = "calculation.txt"
output_file_name = input_file_name
folder_input = "\\input\\"
folder_output = "\\output\\"

input_file = open(current_folder_path + folder_input + input_file_name, "r")

result = parser.parse(input_file.read())

output_file = open(current_folder_path + folder_output + output_file_name, "w")
output_file.write(str(result))

print("Done!")
