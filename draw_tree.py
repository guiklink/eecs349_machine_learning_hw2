# This file will generate a human-readable format of the generated decision tree model

import pydot

graph = pydot.Dot(graph_type='graph')

def makeTree(dtree):
	"""Saves a .png file of the decision tree at root location, requires a dtree to be passed in"""
	visit(dtree)
	graph.write_png('decisionTree.png')

def draw(parent_name, child_name):
	"""Draws a connection between child and parent"""
	edge = pydot.Edge(parent_name, child_name)
	graph.add_edge(edge)


def visit(dtree, parent=None):
	"""Explores the full tree and draws all necessary connections"""
	tags = dtree.fields[0].keys()
	index = 0
	for i in dtree.fields[dtree.parent].keys():
		
		if parent: 
			k1 = dtree.fields[dtree.child0][index]
			k2 = dtree.fields[dtree.child1][index]
			
			print k1,k2,parent
			print ""
			print "i:",i,"index: ",index
			print ""
			if parent and k1: 
				draw(parent, k1)
			if parent and k2:
				draw(parent, k2)
		parent = tags[index]
		index = index+1

		# visit()
