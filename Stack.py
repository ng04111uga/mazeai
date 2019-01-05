"""
					Artificial Intelligence | Fall 2018
		Homework - I | 08 September 2018 | Due: 07 Septmeber 2018
							Narinder Singh
"""

class StackErrors(Exception): pass
class EmptyStackError(Exception): pass

class Stack:
	""" The Stack Data Structure. """

	def __init__(self, items = None):
		""" Initialize the Stack with the given items. Deafault to empty."""
		self._items = items or []

	def push(self, item):
		""" Push the given item onto the stack. """
		self._items.append(item)

	def pop(self):
		""" Pop the topmost item from the stack. """
		return self._items.pop(-1)

	def isEmpty(self):
		""" Return whether the queue is empty or not. """
		return len(self._items) == 0

	def hasItem(self, item):
		""" Return whether the queue has the given item in it. """
		return item in self._items

	def __contains__(self, item):
		""" Delefated to @hasItem mehod. """
		return self.hasItem(item)

	def __str__(self):
		return str(self._items)
	
	def __repr__(self):
		return str(self)

	def __len__(self):
		return len(self._items)
