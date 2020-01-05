#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   10:48 PM -- October 07th, 2019.
#   Project: docit
#   

from docit.util.stringlines import StringLines

class BaseDocItem:

	def __init__(self) -> None:

		self._title: str = ""
		self._description: StringLines = StringLines()
		self._signature: StringLines = StringLines()

	def set_title(self, title: str) -> None:

		self._title = title

	def get_title(self) -> str:

		return "#### `" + self._title + "`"
	
	def get_raw_title(self) -> str:
		
		return self._title

	def set_description(self, description: StringLines) -> None:

		self._description = description

	def get_description(self) -> str:

		return str(self._description)

	def set_signature(self, signature: StringLines) -> None:

		self._signature = signature

	def get_signature(self) -> str:

		return "```typescript\n" + str(self._signature) + "\n```"

	def __str__(self) -> str:

		result = StringLines()

		result.append_line(self.get_title())
		result.append_line()
		result.append_line(self.get_description())
		result.append_line()
		result.append_line(self.get_signature())

		return str(result)