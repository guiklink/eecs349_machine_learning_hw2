# This file just makes a mock decision tree

# 
from tree_util import *
from draw_tree import *
from data_util import *
import pydot


graph = pydot.Dot(graph_type='graph')

dtree = NodePack()

def makeDummyData():
	"""Makes dummy data to validate against.  This dataset is intentionally marked wrong and we expect classification accuracy of 67%"""
	data=importDataCSV("metadata.csv","minidata.csv")
	return data

def makeTree():
	"""Makes a dummy tree"""
	dtree.addNode(1)
	dtree.addNode(2)
	dtree.addNode(3)
	dtree.addNode(4)
	dtree.addNode(5)
	dtree.addNode(6)
	dtree.addNode(7)



	dtree.addParent(2, 1)
	dtree.addParent(3, 1)
	dtree.addParent(4, 3)
	dtree.addParent(5, 3)
	dtree.addParent(6, 4)
	dtree.addParent(7, 4)


	dtree.addChild0(1,2)
	dtree.addChild1(1,3)
	dtree.addChild0(3,4)
	dtree.addChild1(3,5)
	dtree.addChild0(4,6)
	dtree.addChild1(4,7)


	dtree.addNodeType(1,NodeType.ROOT)
	dtree.addNodeType(2,NodeType.LEAF)
	dtree.addNodeType(5,NodeType.LEAF)
	dtree.addNodeType(6,NodeType.LEAF)
	dtree.addNodeType(7,NodeType.LEAF)
	dtree.addNodeType(3,NodeType.EDGE)
	dtree.addNodeType(4,NodeType.EDGE)

	dtree.addSplitType(1, FeatureType.CONTINUOUS)
	dtree.addSplitType(3, FeatureType.CONTINUOUS)
	dtree.addSplitType(4, FeatureType.DISCRETE)

	dtree.addSplitAtribute(1, "winpercent")
	dtree.addSplitAtribute(3, "oppwinpercent")
	dtree.addSplitAtribute(4, "weather")

	dtree.addSplitValue(1,0.5)
	dtree.addSplitValue(3,1)
	dtree.addSplitValue(4,10)

	return dtree

tree = makeTree()
data = makeDummyData()

def validateTree(tree, dataSet):
	"""Used for validating a learned tree against a validation set, returns percentage accuracy"""

	count = 0 #used for tracking how many times we've correctly classified our data
	for index in range(len(dataSet)):
		dataPoint = dataSet[index]
		node = 0
		for i in tree.fields[tree.nType].keys():
			if NodeType.ROOT == tree.getNodeType(i):
				print 'root is equal to ',i
				node = i #basically an index

			#keep going down the tree until no children exist, then get output classification
			while tree.getNodeType(node) != NodeType.LEAF:
				splitVal = tree.getSplitValue(node)
				splitName = tree.getSplitAtribute(node)
				val = dataPoint.retrieve(splitName).getValue()
				if val >= splitVal:
					node = tree.getChild0(node)
				else:
					node = tree.getChild1(node)
				print "So far so good!"
		print "hit a leaf"
		#get tree value (true or false)
		#if treeValue == dataPoint[-1]:
			#count = count + 1
	#print "accuracy is",100*count/len(dataSet)




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