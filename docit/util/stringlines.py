#   
#   Created by Trevor Sears <trevorsears.main@gmail.com>.
#   11:12 PM -- October 07th, 2019.
#   Project: docit
#

from typing import List, Union, Sized

class StringLines:

	def __init__(self, lines: Union[str, List[str], None] = None) -> None:

		self._lines: List[str] = []
		self._iter_index: int = 0

		if lines is not None:

			self.append_line(lines)

	def __len__(self) -> int:

		return len(self._lines)

	def __getitem__(self, item: int) -> str:

		return self._lines[item]

	def __setitem__(self, key: int, value: str) -> None:

		self._lines[key] = value

	def __iter__(self) -> "StringLines":

		self._iter_index = 0
		return self

	def __next__(self) -> str:

		if self._iter_index < len(self._lines):

			result = self._lines[self._iter_index]
			self._iter_index += 1
			return result

		else:

			raise StopIteration

	def __add__(self, other: "StringLines") -> "StringLines":

		if not isinstance(other, StringLines):

			raise TypeError("Attempted to add a non-StringLines item to another StringLines")

		return StringLines(*self._lines, *other)

	def __str__(self) -> str:

		return "\n".join(self._lines)

		# result = ""
		#
		# for line in self._lines:
		#
		# 	if not isinstance(line, str):
		#
		# 		print("ENCOUNTERED NON-STRING")
		# 		print(line)
		#
		# 	result += line + "\n"
		#
		# if len(result) > 0:
		#
		# 	return result[:-1]
		#
		# else:
		#
		# 	return ""

	def append_line(self, line: Union[str, List[str]] = "") -> None:

		if isinstance(line, str):

			self._lines.append(line)

		elif isinstance(line, list):

			for l in line:

				self.append_line(l)

		else:

			raise TypeError("Passed a non-string, non-list value to StringLines#append_line")
