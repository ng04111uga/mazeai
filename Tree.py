"""
					Artificial Intelligence | Fall 2018
	Homework - I | 07 September 2018 | Due: 07 Septmeber 2018 | Narinder Singh

								Node Module
"""

class NodeErrors(Exception): pass
class BadInitialization(NodeErrors): pass

class Node:

	def __init__(self, problem, parent = None, action = None, state = None):
		""" Initilize the new node. If @state is not passed, @parent and @ action are used to determine
		    the new state from the problem definition. """
		if parent is None and state is None: raise BadInitialization() #No way to figure out state
		
		self._parent = parent
		self._action = action
		
		if state is None: self._state = problem.transition(parent.state(), action)
		else: self._state = state
		
		if parent is None: self._pathCost = 0
		else: self._pathCost = parent.pathCost() + problem.stepCost(parent.state(), self.state(), self._action)

	def state(self):
		""" Return the state represented by the node. """
		return self._state

	def action(self):
		""" Return the action that must be taken from the parent to transition to this node. """
		return self._action

	def parent(self):
		""" Return the parent node. """
		return self._parent

	def pathCost(self):
		""" Return the path cost for a path from the "root" to this node."""
		return self._pathCost
	
	def __eq__(self, other):
		if self._parent != other._parent: return False
		if self._action != other._action: return False
		if self._pathCost != other._pathCost: return False
		if self._state != other._state: return False
		return True #Everything Checks

	def __str__(self):
		return str(self.state())

	def __repr__(self):
		return str(self)


def getGoalPath(node):
	""" Construct and return a path from "root" to the given node. """
	if not node: return []
	else: return getGoalPath(node.parent()) + [node.state()]

def getActionSequenceToGoal(node):
	""" Construct and return the action sequence that takes you from "root" to the given node. """
	if not node.parent(): return []
	else: return getActionSequenceToGoal(node.parent()) + [node.action()]


if __name__ == '__main__':
	# Too confident to test.
	# NOTE from future: Should've tested this. Had way too many errors.
	pass

