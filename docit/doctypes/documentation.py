#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   12:07 AM -- October 08th, 2019.
#   Project: docit
#

from typing import List
from docit.doctypes.basedocitem import BaseDocItem

class Documentation:

	def __init__(self) -> None:

		self._documentation_items: List[BaseDocItem] = []

	def add_item(self, item: BaseDocItem) -> None:

		if isinstance(item, BaseDocItem):

			self._documentation_items.append(item)

		else:

			raise TypeError("Attempted to add a non-documentation-item to a Documentation object")

	def __str__(self) -> str:

		return "\n\n---\n\n".join([str(item) for item in self._documentation_items])