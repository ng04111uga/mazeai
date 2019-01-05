"""
					Artificial Intelligence | Fall 2018
		Homework - I | 08 September 2018 | Due: 07 Septmeber 2018
							Narinder Singh
"""

import Search
from Problems import Maze

if __name__ == '__main__':
	maze = Maze()
	
	print 'BREADTH FIRST SEARCH: '
	solution = Search.breadthFirstSearch(maze, verbose=True)
	print solution.summary()
	
	print '\n'
	
	print 'DEPTH FIRST SEARCH: '
	solution = Search.depthFirstSearch(maze, verbose=True)
	print solution.summary()

