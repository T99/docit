#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   5:40 PM -- October 08th, 2019.
#   Project: docit
#

from typing import List as _List
from docit.util import remove_prefix as _remove_prefix

_ACCESS_MODIFIERS: _List[str] = ["public", "protected", "private"]
_TYPE_DECLARATION_KEYWORDS = ["interface", "class", "abstract class", "type"]


def does_string_contain_access_modifiers(string: str) -> bool:
	
	"""
	Returns true if the provided string contains TypeScript-valid access modifiers at the start of the string.
	
	:param string: The string to check for access modifiers.
	:return: true if the provided string contains TypeScript-valid access modifiers at the start of the string.
	"""

	string = string.lstrip()
	return any([string.startswith(modifier) for modifier in _ACCESS_MODIFIERS])
	
def strip_access_modifiers(string: str) -> str:
	
	"""
	Returns a version of the input string from which all TypeScript-valid access modifiers placed at the beginning of
	the string have been removed.
	
	These access modifiers include 'public', 'protected', and 'private'.
	
	:param string: The string from which to strip the access modifiers specified above.
	:return: A version of the input string from which all TypeScript-valid access modifiers placed at the beginning of
	the string have been removed. 
	"""

	for am in _ACCESS_MODIFIERS:

		string = _remove_prefix(string, am + " ")

	return string
	
def strip_property_modifiers(string: str) -> str:

	string = string.replace("static", "", 1)
	string = string.replace("readonly", "", 1)

	return string

def strip_type_declaration_keywords(string: str) -> str:
	
	for tdk in _TYPE_DECLARATION_KEYWORDS:

		string = _remove_prefix(string, tdk + " ")

	return string
	
def is_string_type_declaration(string: str) -> bool:

	return any([string.startswith(keyword) for keyword in _TYPE_DECLARATION_KEYWORDS])
	
def is_string_property_declaration(string: str) -> bool:

	if does_string_contain_access_modifiers(string):

		string = strip_access_modifiers(string)
		string = strip_property_modifiers(string)
		string = string.lstrip()

		next_colon = string.find(":")
		next_space = string.find(" ")
		next_paren = string.find("(")
		
		next_colon = next_colon if next_colon >= 0 else len(string)
		next_space = next_space if next_space >= 0 else len(string)
		next_paren = next_paren if next_paren >= 0 else len(string)

		return next_space > next_colon and next_paren > next_colon

	else:

		return False
	
def extract_type_name(string: str) -> str:
	
	string = strip_type_declaration_keywords(string)

	return string[:min(string.index(" "), string.index("<"))]

def extract_property_name(string: str) -> str:
	
	string = strip_access_modifiers(string)
	string = strip_property_modifiers(string)
	
	return string[:string.index(":")] 

def extract_method_name(string: str) -> str:
	
	string = strip_access_modifiers(string)
	string = _remove_prefix(string, "abstract ")

	return string[:string.index("(")]