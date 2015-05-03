# This is the program for the model generation task augmented
# with a pruning strategy. 
# I.e. It uses the training data to generate a t=decision tree
# and uses the validation set for pruning. 

from tree_util import *
from data_util import *
import model_validate
from tree_gen import InitTree
from copy import *

trainData = importDataCSV("metadata.csv","dummy.csv")
tree = InitTree(trainData)
valData = importDataCSV("metadata.csv","dummyvalidate.csv")

accuracy = model_validate.validateTree(tree, valData)

def pruneTree(tree, valData):
	print "number of edges in unpruned tree: ", countSplits(tree)
	oldAccuracy = 0
	# treeBest = deepcopy(tree)
	treeBest = tree
	newTree = deepcopy(tree)#changed by sherif
	for node in tree.fields[tree.nType].keys():
		if NodeType.UNDEF == tree.getNodeType(node):
			
			newTree.addNodeType(node, NodeType.LEAF) # convert to leaf
			newAccuracy = model_validate.validateTree(newTree, valData)
			# print newAccuracy
			if newAccuracy > oldAccuracy: 
				treeBest = deepcopy(newTree)
				newTree = removeChild(treeBest, node)
				oldAccuracy = newAccuracy
	print "number of edges in pruned tree: ", countSplits(newTree)
	return newTree
					# print "root node: ", node

def removeChild(tree, node):
	parent = tree.getParent(node)
	majClass = tree.getMajorityClassification(node)
	# newTree = deepcopy(tree)
	newTree = tree
	nodeList = [node]
	currentNode = node

	newTree.addNodeType(node, NodeType.LEAF)

	while len(nodeList) > 0 : 
		print "currentNode", currentNode
		if newTree.getNodeType(currentNode) == NodeType.UNDEF: #previous to split EDGE
			child0 = newTree.getChild0(currentNode)
			child1 = newTree.getChild1(currentNode)
			nodeList.append(child0)
			nodeList.append(child1)
		nodeList.pop(0)
		newTree.removeNode(currentNode)
		try:
			currentNode = nodeList[0]
		except: 
			pass
	newTree.addNode(node)
	newTree.addParent(node, parent)
	newTree.addMajorityClassification(node, majClass)
	newTree.addNodeType(node, NodeType.LEAF)

	return newTree

def countSplits(tree):
	count = 1
	for node in tree.fields[tree.nType].keys():
		if tree.getNodeType(node) == NodeType.UNDEF: #previously EDGE
		# if NodeType.EDGE == tree.getNodeType(node):
			count += 1
	return count
