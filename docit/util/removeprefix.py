#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   11:47 AM -- October 08th, 2019.
#   Project: docit
#   

def remove_prefix(text: str, prefix: str) -> str:

	if text.startswith(prefix):

		return text[len(prefix):]

	else:

		return text