# This file makes a mock decision tree
# This file visualizes the generated decision tree
# This file validates a validation set against a decision tree

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

def makeDummyPredictionData():
	"""Makes dummy data to predict for.  This dataset is intentionally marked wrong and we expect classification accuracy of 67%"""
	data=importDataCSV("metadata.csv","minipredict.csv")
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
	dtree.addSplitAtribute(2, "winner")
	dtree.addSplitAtribute(3, "oppwinpercent")
	dtree.addSplitAtribute(4, "weather")
	dtree.addSplitAtribute(5, "winner")
	dtree.addSplitAtribute(6, "winner")
	dtree.addSplitAtribute(7, "winner")

	dtree.addSplitValue(1,0.5)
	dtree.addSplitValue(3,1)
	dtree.addSplitValue(4,10)

	dtree.addDataRowIDs(1, 1)
	dtree.addDataRowIDs(1, 2)
	dtree.addDataRowIDs(1, 3)
	dtree.addDataRowIDs(1, 4)
	dtree.addDataRowIDs(1, 5)
	dtree.addDataRowIDs(1, 6)
	dtree.addDataRowIDs(1, 7)

	dtree.addLeafClassification(2,1)
	dtree.addLeafClassification(5,0)
	dtree.addLeafClassification(6,1)
	dtree.addLeafClassification(7,1)

	return dtree

tree = makeTree()
data = makeDummyData()
dataPre = makeDummyPredictionData()

# def validateTree(tree, dataSet):
# 	"""Used for validating a learned tree against a validation set, returns percentage accuracy"""

# 	count = 0 #used for tracking how many times we've correctly classified our data
# 	for index in range(len(dataSet)):
# 		dataPoint = dataSet[index]
# 		print "Current dataPoint: ", dataPoint.retrieve('id').getValue()
# 		node = 0
# 		for i in tree.fields[tree.nType].keys():
# 			if NodeType.ROOT == tree.getNodeType(i):
# 				node = i #basically an index
# 				print "root node: ", node
# 				break
# 			#keep going down the tree until no children exist, then get output classification

# 		print "node type", tree.getNodeType(node)

# 		while tree.getNodeType(node) != NodeType.LEAF:
# 			splitVal = tree.getSplitValue(node)
# 			print "tree split value: ", splitVal
# 			splitAttribute = tree.getSplitAtribute(node)
# 			print "tree split attribute: ", splitAttribute
# 			val = dataPoint.retrieve(splitAttribute).getValue()
# 			print "data point value for split attribute: ", val
# 			if FeatureType.CONTINUOUS == tree.getSplitType(node): 
# 				if val >= splitVal:
# 					node = tree.getChild0(node)
# 					print "node type", tree.getNodeType(node)
# 					print "greater than", "going to next node", node
# 				else:
# 					node = tree.getChild1(node)
# 					print "lesser than", "going to next node", node
# 					print "node type", tree.getNodeType(node)
# 			elif FeatureType.DISCRETE == tree.getSplitType(node):
# 				if val != splitVal:
# 					node = tree.getChild0(node)
# 					print "not equal", " going to next node", node
# 					print "node type", tree.getNodeType(node)
# 				else:
# 					node = tree.getChild1(node)
# 					print "equal", "goint to next node", node
# 					print "node type", tree.getNodeType(node)
# 		leafClass = tree.getLeafClassification(node)
# 		print "leaf classification: ", leafClass
# 		leafAttribute = tree.getSplitAtribute(node)
# 		print "leaf attribute: ", leafAttribute
# 		print "datapoint classification: ",dataPoint.retrieve(leafAttribute).getValue()
# 		if dataPoint.retrieve(leafAttribute).getValue() == leafClass:
# 			print "correctly classified"
# 			count = count + 1
# 		else: 
# 			print "misclassification"

# 	print "accuracy is: ", float(100*count)/len(dataSet)


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

