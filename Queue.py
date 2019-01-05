"""
					Artificial Intelligence | Fall 2018
		Homework - I | 08 September 2018 | Due: 07 Septmeber 2018
							Narinder Singh
"""

class QueueError(Exception): pass
class EmptyQueueError(Exception): pass

class Queue:
	""" The FIFO Data Structure """

	def __init__(self, items = None):
		""" Initialize the queue with the given list of items. Deafult to an empty queue. """
		self._items = items or []

	def enqueue(self, item):
		""" Enqueue the given item to the queue. """
		self._items.append(item)

	def dequeue(self):
		""" Dequeue and return an item from the queue respecting FIFO ordering. """
		if self.isEmpty(): raise EmptyQueueError()
		return self._items.pop(0)

	def isEmpty(self):
		""" Return whether the queue is empty. """
		return len(self._items) == 0

	def hasItem(self, item):
		""" Return whether the queue has the given item in it. """
		return item in self._items

	def __contains__(self, item):
		""" Implemented by @hasItem mehod. """
		return self.hasItem(item)
	
	def __str__(self):
		return str(self._items)

	def __repr__(self):
		return str(self)

	def __len__(self):
		return len(self._items)
