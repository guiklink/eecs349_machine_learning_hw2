# This file will generate a human-readable format of the generated decision tree model
from tree_util import *
import pydot
import sets

graph = pydot.Dot(graph_type='graph')

def makeTree(dtree, fileName):
	"""Saves a .png file of the decision tree at root location, requires a dtree to be passed in"""
	draw(dtree)
	graph.write_png(fileName)

def draw(dtree, node=None):
	"""Explores all nodes in a tree and builds a visual tree as a png file in root"""
	tags = dtree.fields[dtree.parent].keys()  #returns a list of node names
	pairs = []
	pair = sets.Set([])
	toggle = True
	#go through each instance of tag and try writing a line between parent and child
	for node in tags:
		parent = dtree.fields[dtree.parent][node]
		if parent == None:
			print "no parent"
		else: 
			pair = sets.Set([node, parent])
			pairs.append(pair)

		# k1 = dtree.fields[dtree.child0][node]
		# if k1 != None:
		# 	pair = sets.Set([node, k1])
		# 	pairs.append(pair)
		# else: 
		# 	print "no child for node ", node

		# k2 = dtree.fields[dtree.child1][node] 
		# if k2 != None: 
		# 	pair = sets.Set([node, k2])
		# 	pairs.append(pair)	
		# else: 
		# 	print "no child for node ", node		

		if node and parent:
			for i in range(len(pairs)-1):
				if pair == pairs[i]: 
					print "found pari"
					toggle = False
			if toggle:
				# draw(node, k1, dtree)
				parentnode = pydot.Node(dtree.getSplitAtribute(parent), style="filled", fillcolor="blue")
				graph.add_node(parentnode)
				childnode = pydot.Node(node,style="filled", fillcolor="blue")
				if FeatureType.CONTINUOUS == dtree.getSplitType(parent): 
					pass
					graph.add_edge(pydot.Edge(parentnode, childnode, lable =" <= "))
				else:
					graph.add_edge(pydot.Edge( parentnode, childnode, lable =" != "))
				toggle = True


		# if node and k2:
		# 	for i in range(len(pairs)-1):
		# 		if pair == pairs[i]: 
		# 			toggle = False
		# 	if toggle:
		# 		# draw(node, k1, dtree)
		# 		parentnode = pydot.Node(dtree.getSplitAtribute(node), style="filled", fillcolor="blue")
		# 		graph.add_node(parentnode)
		# 		childnode = pydot.Node(dtree.fields[dtree.child0][node])
		# 		if FeatureType.CONTINUOUS == dtree.getSplitType(node): 
		# 			graph.add_edge(pydot.Edge( parentnode, childnode, lable =" > "))
		# 		else:
		# 			graph.add_edge(pydot.Edge( parentnode, childnode, lable =" = "))
		# 		toggle = True
