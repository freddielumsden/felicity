import lexer
import converter

file_name = "examplefile"  # input("File Name: ")
with open(file_name, 'r') as f:
    file = f.read()
lexed_file = lexer.lexer(file)
if isinstance(lexed_file, list):
	print("Lexed File:", lexed_file)
	converted_file = converter.converter(lexed_file)
	print("Converted File:", converted_file)
else:
	print(lexed_file)