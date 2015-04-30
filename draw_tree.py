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


def visit(dtree, node=None):
	"""Explores all nodes in a tree and builds a visual tree as a png file in root"""
	tags = dtree.fields[dtree.parent].keys()  #returns a list of node names
	
	#go through each instance of tag and try writing a line between parent and child
	for node in tags:		
		try:
			k1 = dtree.fields[dtree.child0][node]
			k2 = dtree.fields[dtree.child1][node]
		except:
			print "no child"

		if node and k1:
			draw(node,k1)
		if node and k2:
			draw(node,k2)
