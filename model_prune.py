# This is the program for the model generation task augmented
# with a pruning strategy. 
# I.e. It uses the training data to generate a t=decision tree
# and uses the validation set for pruning. 

from tree_util import *
from data_util import *
# from model_validate import *
import model_validate
import mockTree

tree = mockTree.makeTree()
data = mockTree.makeDummyData()

accuracy = model_validate.validateTree(tree, data)

def pruneTree(tree, dataSet, accuracy):
	prunedTree = tree

	for i in prunedTree.fields[prunedTree.nType].keys():
			# find a leaf
			if NodeType.LEAF == prunedTree.getNodeType(i):
				leaf = i
				prunedTree.addNodeType(leaf, NodeType.UNDEF) # Ignore current leaf
				newAccuracy = model_validate.validateTree(prunedTree, dataSet)

				if newAccuracy < accuracy:
					prunedTree.addNodeType(leaf, NodeType.LEAF) # add current leaf
	return prunedTree




	