# This file contains all the structures and functions for the tree

# Importing...

from tree_util import *
from data_util import *
from csv_handler import *

# GLOBAL NODE TAGGER
rootNode = 0
nodeCount = rootNode + 1


# INIT TREE ###################################################################################

# Def

# Entry ->
# Returns ->

def InitTree():
	global rootNode
	rawTable = importDataCSV("metadata.csv","dummy.csv")

	nodePack = NodePack()

	nodePack.addNode(rootNode)
	nodePack.addDataRowIDs(rootNode,distinctAtributes(rawTable,"id"))
	nodePack.addNodeType(rootNode,NodeType.EDGE)

	BuildTree(nodePack, rawTable)


###############################################################################################

# MAKE CHILD ##################################################################################

# Def

# Entry ->
# Returns ->

def makeChild(nodePack ,childTag, parentTag, parentDataRowIDs):
	nodePack.addNode(childTag)
	nodePack.addParent(childTag, parentTag)
	nodePack.addDataRowIDs(childTag, parentDataRowIDs)
	nodePack.addNodeType(childTag, NodeType.EDGE)


###############################################################################################

# BUILD TREE ##################################################################################

# Def

# Entry ->
# Returns ->

def BuildTree(nodePack, rawTable):
	global rootNode, nodeCount;

	while len(nodePack.retrieveListOfNodesByType(NodeType.EDGE)) != 0:
		edgeNodes = nodePack.retrieveListOfNodesByType(NodeType.EDGE)

		for nodeTag in edgeNodes:
			if nodePack.getNodeEntropy(nodeTag, rawTable) < leafEntropy:
				nodePack.addNodeType(nodeTag,NodeType.LEAF)

		splitNodeTag,splitFeature,splitValue,nmj = nodePack.bestSplit(1000,rawTable)

		# Create child 0
		nodeCount += 1
		makeChild(nodePack, nodeCount, nodeTag, nmj[0])
		nodePack.addChild0(nodeTag,nodeCount)

		# Create child 1
		nodeCount += 1
		makeChild(nodePack, nodeCount, nodeTag, nmj[1])
		nodePack.addChild1(nodeTag,nodeCount)

		# Update Parent fields
		nodePack.addSplitType(rawTable[0].retrieve(splitFeature).fType)

		if rootNode == nodeTag:
			nodePack.addNodeType(nodeTag,NodeType.ROOT)
		else:
			nodePack.addNodeType(nodeTag,NodeType.UNDEF)

		nodePack.addSplitAtribute(nodeTag,splitFeature)
		nodePack.addSplitValue(nodeTag, splitValue)
	return nodePack



###############################################################################################


if __name__ == '__main__':
	leafEntropy = 0.1

	InitTree()