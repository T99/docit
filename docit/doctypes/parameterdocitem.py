#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   10:24 PM -- October 08th, 2019.
#   Project: docit
#   

from typing import List, Tuple
from docit.util import StringLines
from .basedocitem import BaseDocItem

class ParameterDocItem(BaseDocItem):
	
	def __init__(self) -> None:
		
		super().__init__()
		
		self._parameters: List[Tuple[str, str]] = []

	def add_parameter(self, param: str, description: str) -> None:

		self._parameters.append((param, description))

	def get_parameters(self) -> str:

		result = StringLines()

		result.append_line("**Parameters**:")

		if len(self._parameters) <= 0:

			result.append_line(" - _None_")

		else:

			for parameter in self._parameters:

				result.append_line(" - **" + parameter[0] + "** " + parameter[1])

		return str(result)
	
	def __str__(self) -> str:

		result = StringLines()

		result.append_line(self.get_title())
		result.append_line()
		result.append_line(self.get_description())
		result.append_line()
		result.append_line(self.get_parameters())
		result.append_line()
		result.append_line(self.get_signature())

		return str(result)