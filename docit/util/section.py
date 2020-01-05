#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   4:32 PM -- October 08th, 2019.
#   Project: docit
#

from docit.util import StringLines

class Section:

	def __init__(self) -> None:

		self.body: StringLines = StringLines()
		self.signature: StringLines = StringLines()