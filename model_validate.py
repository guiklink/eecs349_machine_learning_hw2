# This is a program that validates the model generated by 
# model-train based on the validation set. 

from tree_util import *
from data_util import *
import mockTree


tree = mockTree.makeTree()
data = mockTree.makeDummyData()

def validateTree(tree, dataSet):
	"""Used for validating a learned tree against a validation set, returns percentage accuracy"""
	print "validateTree called"
	count = 0 #used for tracking how many times we've correctly classified our data
	for index in range(len(dataSet)):
		dataPoint = dataSet[index]
		# print "Current dataPoint: ", dataPoint.retrieve('id').getValue()
		node = 0
		for i in tree.fields[tree.nType].keys():
			if NodeType.ROOT == tree.getNodeType(i):
				node = i #basically an index
				# print "root node: ", node
				break
			#keep going down the tree until no children exist, then get output classification

		# print "node type", tree.getNodeType(node)

		while tree.getNodeType(node) != NodeType.LEAF and tree.getNodeType(node) != NodeType.UNDEF:
			
			splitVal = tree.getSplitValue(node)
			# print "tree split value: ", splitVal
			splitAttribute = tree.getSplitAtribute(node)
			# print "tree split attribute: ", splitAttribute
			val = dataPoint.retrieve(splitAttribute).getValue()
			# print "data point value for split attribute: ", val
			if FeatureType.CONTINUOUS == tree.getSplitType(node): 
				if val >= splitVal:
					node = tree.getChild0(node)
					# print "node type", tree.getNodeType(node)
					# print "greater than", "going to next node", node
				else:
					node = tree.getChild1(node)
					# print "lesser than", "going to next node", node
					# print "node type", tree.getNodeType(node)
			elif FeatureType.DISCRETE == tree.getSplitType(node):
				if val != splitVal:
					node = tree.getChild0(node)
					# print "not equal", " going to next node", node
					# print "node type", tree.getNodeType(node)
				else:
					node = tree.getChild1(node)
					# print "equal", "goint to next node", node
					# print "node type", tree.getNodeType(node)

		if tree.getNodeType(node)== NodeType.LEAF:
			leafClass = tree.getLeafClassification(node)
			# print "leaf classification: ", leafClass
			leafAttribute = tree.getSplitAtribute(node)
			# print "leaf attribute: ", leafAttribute
			# print "datapoint classification: ",dataPoint.retrieve(leafAttribute).getValue()
			if dataPoint.retrieve(leafAttribute).getValue() == leafClass:
				count = count + 1
			
				
	accuracy = float(100*count)/len(dataSet)
	print "accuracy is: ", accuracy


	return accuracy


