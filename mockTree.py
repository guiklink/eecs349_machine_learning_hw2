# This file just makes a mock decision tree

# 
from tree_util import *
from draw_tree import *
import pydot


graph = pydot.Dot(graph_type='graph')

dtree = NodePack()

dtree.addNode("root")
dtree.addNode("child")
dtree.addNode(3)
dtree.addNode(4)
dtree.addNode(5)
dtree.addNode(6)
dtree.addNode(7)
dtree.addNode("leaf")


dtree.addParent("child", "root")
dtree.addParent(3, "root")
dtree.addParent(4, "child")
dtree.addParent(5, "child")
dtree.addParent(6, 3)
dtree.addParent(7, 3)
dtree.addParent("leaf", 7)


dtree.addChild0("root","child")
dtree.addChild1("root",3)
dtree.addChild0("child",4)
dtree.addChild1("child",5)
dtree.addChild0(3,6)
dtree.addChild1(3,7)
dtree.addChild1(7,"leaf")

def draw(parent_name, child_name):
	edge = pydot.Edge(parent_name, child_name)
	graph.add_edge(edge)



def visit(dtree, node=None):

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

if __name__ == '__main__':
	visit(dtree)
	graph.write_png('example1_graph.png')




# def visit(dtree, parent=None):

# 	tags = dtree.fields[0].keys()
# 	for i in range(len(dtree.fields[dtree.parent].keys())):
# 	# for i in range(3):
# 		k1 = dtree.fields[dtree.child0][i+1]
# 		k2 = dtree.fields[dtree.child1][i+1]
# 		parent = tags[i]
# 		print k1,k2,parent
# 		print ""
# 		if parent and k1:
# 			draw(parent, k1)
# 		if parent and k2: 
# 			draw(parent, k2)
# 		# visit()