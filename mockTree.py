# This file just makes a mock decision tree

# 
from tree_util import *
from draw_tree import *
import pydot


graph = pydot.Dot(graph_type='graph')

dtree = NodePack()

dtree.addNode('root')
dtree.addNode(2)
dtree.addNode(3)
dtree.addNode(4)
dtree.addNode(5)
dtree.addNode(6)
dtree.addNode(7)
dtree.addNode(8)


dtree.addParent(2, 1)
dtree.addParent(3, 1)
dtree.addParent(4, 2)
dtree.addParent(5, 2)
dtree.addParent(6, 3)
dtree.addParent(7, 3)
dtree.addParent(8, 7)


dtree.addChild0(1,2)
dtree.addChild1(1,3)
dtree.addChild0(2,4)
dtree.addChild1(2,5)
dtree.addChild0(3,6)
dtree.addChild1(3,7)
dtree.addChild1(7,8)

def draw(parent_name, child_name):
	edge = pydot.Edge(parent_name, child_name)
	graph.add_edge(edge)


def visit(dtree, parent=None):

	tags = dtree.fields[0].keys()
	for i in range(len(dtree.fields[dtree.parent].keys())):
	# for i in range(3):
		k1 = dtree.fields[dtree.child0][i+1]
		k2 = dtree.fields[dtree.child1][i+1]
		parent = tags[i]
		print k1,k2,parent
		print ""
		if parent and k1 and k2: 
			draw(parent, k1)
			draw(parent, k2)
		# visit()


	

if __name__ == '__main__':
	visit(dtree)
	graph.write_png('example1_graph.png')

