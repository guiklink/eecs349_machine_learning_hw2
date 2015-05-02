# This is a program that validates the model generated by 
# model-train based on the validation set. 

from tree_util import *
from data_util import *
import mockTree
import numpy as np

tree = mockTree.makeTree()
valdata = importDataCSV("metadata.csv","minidata.csv")

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

		# while tree.getNodeType(node) != NodeType.LEAF and tree.getNodeType(node) != NodeType.UNDEF:
		while tree.getNodeType(node) != NodeType.LEAF:
			splitVal = tree.getSplitValue(node)
			# print "tree split value: ", splitVal
			splitAttribute = tree.getSplitAtribute(node)
			# print "tree split attribute: ", splitAttribute
			val = dataPoint.retrieve(splitAttribute).getValue()

			if val == None:		
				val = np.median(retrieveDataFromColumn(dataSet, splitAttribute))

			if FeatureType.CONTINUOUS == tree.getSplitType(node): 
				if val < splitVal:
					node = tree.getChild0(node)

				else:
					node = tree.getChild1(node)

			elif FeatureType.DISCRETE == tree.getSplitType(node):
				if val != splitVal:
					node = tree.getChild0(node)

				else:
					node = tree.getChild1(node)

		if tree.getNodeType(node)== NodeType.LEAF:
			leafClass = tree.getMajorityClassification(node)
			if dataPoint.retrieve('winner').getValue() == leafClass:
				count = count + 1
			
				
	accuracy = float(100*count)/len(dataSet)
	print "accuracy is: ", accuracy


	return accuracy