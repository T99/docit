#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   11:49 AM -- October 08th, 2019.
#   Project: docit
#   

from sys import argv
from os import path

from docit.packageinfo import NAME, VERSION
from docit.util import remove_prefix, StringLines, Section
from docit.doctypes import Documentation, BaseDocItem, MethodDocItem, ConstructorDocItem
from docit.lang.typescript.util import strip_access_modifiers, is_string_type_declaration,\
	is_string_property_declaration, strip_property_modifiers, extract_method_name, extract_type_name,\
	extract_property_name

from typing import List, Tuple, Union

def print_help_message() -> None:

	print(NAME + " " + VERSION)
	print("Usage: docit <input_file>")

def get_file_path() -> str:
	
	arguments = argv[1:]
	number_of_args = len(arguments)

	if number_of_args <= 0:

		print_help_message()
		exit(0)

	elif number_of_args < 1:

		print("Too few arguments!\n")
		print_help_message()
		exit(1)

	elif number_of_args > 1:

		print("Too many arguments!\n")
		print_help_message()
		exit(1)

	return arguments[0]

def read_in_lines(file_path: str) -> List[str]:

	if not path.exists(file_path):
		print("The file '" + file_path + "' could not be found.")
		exit(1)

	if not path.isfile(file_path):
		print("The provided 'file' ('" + file_path + "') was actually a directory.")
		exit(1)

	with open(file_path) as file:

		data = file.read()
		return data.splitlines()

def print_sections(sections: List[Section]) -> None:

	for section in sections[:-1]:

		print(str(section.body))
		print(str(section.signature))
		print("\n" * 2)

	print(str(sections[-1].body))
	print(str(sections[-1].signature))

def run(input_file_path: str = get_file_path()) -> None:

	lines = read_in_lines(input_file_path)

	lines = [line.strip() for line in lines]

	sections: List[Section] = []

	current_section: Section = Section()
	is_section = False
	is_signature = False

	# Parse sections out of raw lines of file.
	for line in lines:

		if is_section:

			if line.startswith("*/"):

				sections.append(current_section)
				is_section = False
				is_signature = True

			else:

				current_section.body.append_line(line)

		elif is_signature:

			current_section.signature.append_line(remove_prefix(line, "export "))

			if line.endswith("{") or line.endswith(";"):

				if line.endswith("{"):

					current_section.signature[-1] = current_section.signature[-1] + " ... }"

				current_section = Section()

				is_signature = False

		elif line.startswith("/**"):

			is_section = True

	for section in sections:

		section.body = StringLines([line.lstrip("* ") for line in section.body])

	documentation = Documentation()

	for section in sections:

		signature = "".join(section.signature)

		if is_string_type_declaration(signature):

			doc_item = BaseDocItem()
			title = extract_type_name(signature)
			
		elif is_string_property_declaration(signature):

			doc_item = BaseDocItem()
			title = extract_property_name(signature)

		else:

			title = extract_method_name(signature)
			
			if title == "constructor":
				
				doc_item = ConstructorDocItem()
				
			else:
				
				doc_item = MethodDocItem()

				return_lines = [remove_prefix(line, "@return ") for line in section.body if line.startswith("@return")]

				if len(return_lines) == 1:

					doc_item.set_return(return_lines[0])

				elif len(return_lines) > 1:

					raise ValueError("More than one @return statement was encountered in a single doc-comment")

			param_lines = [remove_prefix(line, "@param ") for line in section.body if line.startswith("@param")]

			for param_line in param_lines:

				param_name = param_line[:param_line.index(" ")]
				param_desc = param_line[param_line.index(" ") + 1:]

				doc_item.add_parameter(param_name, param_desc)

		desc_lines: List[str] = []

		for line in section.body:
			
			if not line.startswith("@"):

				if len(desc_lines) > 0 and desc_lines[-1] != "":
					
					desc_lines[-1] = desc_lines[-1] + " " + line
					
				else:
					
					desc_lines.append(line)

			else:

				break

		if len(desc_lines) > 0 and desc_lines[-1] == "":

			desc_lines.pop()

		doc_item.set_title(title)

		doc_item.set_description(StringLines(desc_lines))

		doc_item.set_signature(StringLines([signature]))

		documentation.add_item(doc_item)

	print(documentation)