"""
					Artificial Intelligence | Fall 2018
		Homework - I | 08 September 2018 | Due: 07 Septmeber 2018
							Narinder Singh
"""

import Tree
from Tree import Node
from Queue import Queue
from Stack import Stack

class SearchErrors(Exception): pass
class NoSolutionFoundError(SearchErrors): pass

class Solution(Exception):
	""" Describes a solution of a search algorithm by tracking the progress of a search algorithm. """

	def __init__(self, verbose = False):
		""" Initialize the instance with runtime given characterisitics. """
		self._algorithm = ''
		self._maxFrontierSize = 0
		self._maxExploredSetSize = 0
		self._verbose = verbose
		self._goalNode = None
	
	def trackProgress(self, frontier, exploredSet = []):
		""" Track the runtime performance of the  """
		self._maxFrontierSize = max(self.getMaxFrontierSize(), len(frontier))
		self._maxExploredSetSize = max(self.getMaxExploredSetSize(), len(exploredSet))
		
		if self._verbose:
			print 'Frontier: ' + str(frontier)
			print 'Explored Set: ' + str(exploredSet) + '\n'

	def getMaxFrontierSize(self):
		""" Return maximum size that the fronier grew up to so far. """
		return self._maxFrontierSize

	def getMaxExploredSetSize(self):
		""" Return maximum size that the explored set grew up to so far. """
		return self._maxExploredSetSize

	def getGoalNode(self):
		""" Return goal node as set by the search algorithm. """
		return self._goalNode

	def setGoalNode(self, goal):
		""" Set the goal node. """
		self._goalNode = goal
		return self

	def getGoalPath(self):
		""" Construct and return a path from "root" to the given node. """
		return Tree.getGoalPath(self.getGoalNode())

	def getActionSequenceToGoal(self):
		""" Construct and return the action sequence that takes you from "root" to the given node. """
		return Tree.getActionSequenceToGoal(self.getGoalNode())

	def summary(self):
		""" Summarises the solution. """
		goalPath = 'Goal Path: ' + ', '.join([str(x) for x in self.getGoalPath()])
		actionSequence = 'Action Sequence: ' + ', '.join([str(x) for x in self.getActionSequenceToGoal()])
		maxFrontier = 'Maximum Frontier size: ' + str(self.getMaxFrontierSize())
		maxExplored = 'Maximum Explored Set size: ' + str(self.getMaxExploredSetSize())
		
		return '\n'.join([goalPath, actionSequence, maxFrontier, maxExplored])


def breadthFirstSearch(problem, verbose=False):
	""" Perform a Breadth-First search on the given problem and return a solution.
		NOTE: This is a graph based implementation of the algorithm, please be aware of the memory overhead."""
	start = Node(problem, state = problem.initialState())
	solution = Solution(verbose)

	if problem.goalTest(start.state()): return solution.setGoalNode(start)
	frontier = Queue(items=[start])
	explored = set()
	
	while True:
		solution.trackProgress(frontier, explored)
		if frontier.isEmpty(): raise NoSolutionFoundError()
		node = frontier.dequeue()
		explored.add(node.state())
		for action in problem.applicableActions(node.state()):
			child = Node(problem, node, action)
			if child not in frontier and child.state() not in explored:
				if problem.goalTest(child.state()): return solution.setGoalNode(child)
				else: frontier.enqueue(child)


def depthFirstSearch(problem, verbose=False):
	""" Perform a Depth-First search on the given problem and return a solution.
		NOTE: This is a graph based implementation of the algorithm, please be aware of the memory overhead."""
	start = Node(problem, state = problem.initialState())
	solution = Solution(verbose)

	if problem.goalTest(start.state()): return solution.setGoalNode(start)
	frontier = Stack(items=[start])
	explored = set()

	while True:
		solution.trackProgress(frontier, explored)
		if frontier.isEmpty(): raise NoSolutionFoundError()
		node = frontier.pop()
		explored.add(node.state())

		for action in problem.applicableActions(node.state()):
			child = Node(problem, node, action)
			if child not in frontier and child.state() not in explored:
				if problem.goalTest(child.state()): return solution.setGoalNode(child)
				frontier.push(child)










