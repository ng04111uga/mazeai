"""
					Artificial Intelligence | Fall 2018
	Homework - I | 07 September 2018 | Due: 07 Septmeber 2018 | Narinder Singh

							Problems Module
"""

class ProblemsError(Exception):	pass
class BadTransitionError(ProblemsError): pass
class BadStateError(ProblemsError): pass

class Maze:
	""" Characteriztion of the Maze from the Assignment as a state space. """
	_states = range(25) #Set of possible states
	_stepCost = 1 #Uniform step-cost.
	_goalState = 17 #End of the maze.
	_stateTransitionMap = { #Adjacency list.
		0: [1, 2],
		1: [0],
		2: [3, 4, 0],
		3: [2],
		4: [2, 8, 5],
		5: [7, 6, 4],
		6: [5],
		7: [5],
		8: [9, 10, 4],
		9: [8],
		10: [12, 11, 8],
		11: [10, 14, 13],
		12: [10],
		13: [11],
		14: [15, 11, 16],
		15: [14],
		16: [14, 17, 18],
		17: [16],
		18: [16, 20, 19],
		19: [18],
		20: [21, 18, 22],
		21: [20],
		22: [20, 24, 23],
		23: [22],
		24: [22]
	} #NOTE: The action is represented as the resulting state i.e., action = resulting state.

	def __init__(self, initialState = 0):
		""" Initilize the Maze object with starting state. Defaults to Start position. """
		self._initialState = initialState

	def states(self):
		""" A list of the possible set of states in the search space. """
		return self._states

	def initialState(self):
		""" Return the initialState as set during initialization. """
		return self._initialState

	def applicableActions(self, state):
		""" Return the set of applicable actions in the given state. """
		if state not in self._stateTransitionMap: raise BadStateError()
		else: return self._stateTransitionMap[state]

	def transition(self, state, action):
		""" Return the new state an agent would be in after performing the given action in the given state.
		    A None type action is takes to imply no transition. """
		if action is None: return state
		if action not in self.applicableActions(state): raise BadTransitionError()
		else: return action

	def stepCost(self, frm, to, action):
		""" The cost to transiton between the given states through the given action."""
		if frm not in self._states or to not in self._states: raise BadStateError() #Invalid input states
		if to != action: raise BadTransitionError() #Invalid transition. Refer NOTE of _stateTransitonMap.
		if to not in self._stateTransitionMap[frm]: raise BadTransitionError() #Invalid transition.
		return self._stepCost

	def goalTest(self, state):
		""" Return wether or not the given state is the goal state. """
		if state not in self._states: raise BadStateError()
		return state == self._goalState

if __name__ == '__main__':
	# Quick and Dirty testing. Unit testing not worth the time here.
	prb = Maze()
	print prb.states() == range(25)
	print prb.initialState() == 0
	print prb.applicableActions(3) == [2]
	print prb.transition(22, 23) == 23
	print prb.stepCost(2, 4, 4) == 1
	print prb.goalTest(12) is False
	print prb.goalTest(17) is True


	

