#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   11:54 PM -- October 07th, 2019.
#   Project: docit
#

from typing import List, Tuple
from docit.util.stringlines import StringLines
from .parameterdocitem import ParameterDocItem

class MethodDocItem(ParameterDocItem):

	def __init__(self) -> None:

		super().__init__()

		self._parameters: List[Tuple[str, str]] = []
		self._returns = "Void."

	def get_title(self) -> str:
		
		return "#### `#" + self._title + "`"

	def set_return(self, returns: str) -> None:

		self._returns = returns

	def get_return(self) -> str:

		return "**Returns** " + self._returns

	def __str__(self) -> str:

		result = StringLines()

		result.append_line(self.get_title())
		result.append_line()
		result.append_line(self.get_description())
		result.append_line()
		result.append_line(self.get_parameters())
		result.append_line()
		result.append_line(self.get_return())
		result.append_line()
		result.append_line(self.get_signature())

		return str(result)

