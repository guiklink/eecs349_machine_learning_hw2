# This file will generate a human-readable format of the generated decision tree model

import pydot
import sets

graph = pydot.Dot(graph_type='graph')

def makeTree(dtree, fileName):
	"""Saves a .png file of the decision tree at root location, requires a dtree to be passed in"""
	visit(dtree)
	graph.write_png(fileName)

def draw(parent_name, child_name):
	"""Draws a connection between child and parent"""
	edge = pydot.Edge(parent_name, child_name)
	graph.add_edge(edge)


def visit(dtree, node=None):
	"""Explores all nodes in a tree and builds a visual tree as a png file in root"""
	tags = dtree.fields[dtree.parent].keys()  #returns a list of node names
	pairs = []
	pair = sets.Set([])
	toggle = True
	#go through each instance of tag and try writing a line between parent and child
	# for node in tags:		
	# 	try:
	# 		k1 = dtree.fields[dtree.child0][node]
	# 		k2 = dtree.fields[dtree.child1][node]
	# 	except:
	# 		print "no child"

	# 	if node and k1:
	# 		draw(node,k1)
	# 	if node and k2:
	# 		draw(node,k2)
	for node in tags:
		parent = dtree.fields[dtree.parent][node]
		pair = sets.Set([node, parent])
		pairs.append(pair)
		if parent == None:
			print "no parent"

		if node and parent: 
			for i in range(len(pairs)-1):
				if pair == pairs[i]: 
					toggle = False
			if toggle:
				draw(parent, node)
				toggle = True