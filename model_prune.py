# This is the program for the model generation task augmented
# with a pruning strategy. 
# I.e. It uses the training data to generate a t=decision tree
# and uses the validation set for pruning. 

from tree_util import *
from data_util import *
import draw_tree
# from model_validate import *
import model_validate
import mockTree
from copy import *

tree = mockTree.makeTree()
data = importDataCSV("metadata.csv","minidata.csv")

accuracy = model_validate.validateTree(tree, data)

# def pruneTree(tree, dataSet, accuracy):
# 	prunedTree = deepcopy(tree)

# 	for i in prunedTree.fields[prunedTree.nType].keys():
# 			# find a leaf
# 			if NodeType.LEAF == prunedTree.getNodeType(i):
# 				leaf = i
# 				prunedTree.addNodeType(leaf, NodeType.UNDEF) # Ignore current leaf
# 				newAccuracy = model_validate.validateTree(prunedTree, dataSet)

# 				if newAccuracy < accuracy:
# 					prunedTree.addNodeType(leaf, NodeType.LEAF) # add current leaf
# 	return prunedTree


def pruneTree(tree, valData):
	print "number of edges in unpruned tree: ", countEdges(tree)
	oldAccuracy = 0
	# treeBest = deepcopy(tree)
	treeBest = tree
	for node in tree.fields[tree.nType].keys():
		if NodeType.EDGE == tree.getNodeType(node):
			newTree = deepcopy(tree)
			newTree.addNodeType(node, NodeType.LEAF) # convert to leaf
			newAccuracy = model_validate.validateTree(newTree, valData)
			# print newAccuracy
			if newAccuracy > oldAccuracy: 
				treeBest = deepcopy(newTree)
				newTree = removeChild(treeBest, node)
				oldAccuracy = newAccuracy
	print "number of edges in pruned tree: ", countEdges(newTree)
	return newTree
					# print "root node: ", node

def removeChild(tree, node):
	parent = tree.getParent(node)
	majClass = tree.getMajorityClassification(node)
	# newTree = deepcopy(tree)
	newTree = tree
	nodeList = [node]
	currentNode = node

	newTree.addNodeType(node, NodeType.EDGE)

	while len(nodeList) > 0 : 
		if newTree.getNodeType(currentNode) == NodeType.EDGE:
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

def countEdges(tree):
	count = 1
	for node in tree.fields[tree.nType].keys():
		if tree.getNodeType(node) == NodeType.EDGE:
		# if NodeType.EDGE == tree.getNodeType(node):
			count += 1
	return count



	