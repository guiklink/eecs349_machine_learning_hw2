# This file contains all the structures and functions for the tree

# Importing...

from tree_util import *
from data_util import *
from csv_handler import *

# GLOBAL NODE TAGGER
rootNode = 0
nodeCount = rootNode 


# INIT TREE ###################################################################################

# Def

# Entry ->
# Returns ->

def InitTree(rawTable):
	global rootNode

	nodePack = NodePack()

	nodePack.addNode(rootNode)
	nodePack.addDataRowIDs(rootNode,distinctAtributes(rawTable,"id"))
	nodePack.addNodeType(rootNode,NodeType.EDGE)
	a=BuildTree(nodePack, rawTable)
	# nodePack.printNodePack()
	return a


###############################################################################################

# MAKE CHILD ##################################################################################

# Def

# Entry ->
# Returns ->

def makeChild(nodePack ,childTag, parentTag, nmj):
	nodePack.addNode(childTag)
	nodePack.addParent(childTag, parentTag)

	if len(nmj) == 0:
		raise NameError('This node has no instances and wont classify anything!')
	else:
		newIDs = distinctAtributes(nmj,"id")

	nodePack.addDataRowIDs(childTag, newIDs)
	nodePack.addNodeType(childTag, NodeType.EDGE)


###############################################################################################

# BUILD TREE ##################################################################################

# Def

# Entry ->
# Returns ->

def BuildTree(nodePack, rawTable):
	global rootNode, nodeCount;
	splittedDiscrete = []
	splittedValue = []

	terminationCounter=0
	prevNodePackSize= len(nodePack.fields[0].keys())
	while len(nodePack.retrieveListOfNodesByType(NodeType.EDGE)) != 0 and terminationCounter < 2:
		
		print '>> Generating ...'

		edgeNodes = nodePack.retrieveListOfNodesByType(NodeType.EDGE)

		# print '\n\nAll nodes'
		# print nodePack.fields[0].keys()
		# print '\n\n ****** ROOT'
		# print nodePack.retrieveNodesByType(NodeType.ROOT)

		# print '\n\n ****** ALL LEAF NODES'
		# print nodePack.retrieveNodesByType(NodeType.LEAF)

		# print '\n\n ****** ALL EDGE NODES'
		# print nodePack.retrieveNodesByType(NodeType.EDGE)

		# print '\n\n ****** ALL UNDEF NODES'
		# print nodePack.retrieveNodesByType(NodeType.UNDEF)
		
		# nodePack.printNodePack()

		# w=input('\n\nWaiting... ')

		for nodeTag in edgeNodes:
			if nodePack.getNodeEntropy(nodeTag, rawTable) < 0.1:
				#print '******** CREATING LEAF*****************'
				#print nodeTag
				nodePack.addNodeType(nodeTag,NodeType.LEAF)
		#print 'Node:' + str(nodeCount) + ' | Entropy = ' + str(nodePack.getNodeEntropy(nodeCount, rawTable)) 

		if len(nodePack.fields[0].keys()) == prevNodePackSize:
			terminationCounter+=1

		splitNodeTag,splitFeature,splitValue,nmj = nodePack.bestSplit(1000,rawTable,splittedDiscrete,splittedValue)

		prevNodePackSize = len(nodePack.fields[0].keys())
		if nmj[0] != [] and nmj[1] != []:
			splittedValue.append((splitFeature,splitValue))

			# add discrete value to a list, we do not want do them again
			if rawTable[0].retrieve(splitFeature).fType == FeatureType.DISCRETE:
				splittedDiscrete.append(splitFeature)

			# Create child 0
			nodeCount += 1
			makeChild(nodePack, nodeCount, nodeTag, nmj[0])
			nodePack.addChild0(nodeTag,nodeCount)

			# Create child 1
			nodeCount += 1
			makeChild(nodePack, nodeCount, nodeTag, nmj[1])
			nodePack.addChild1(nodeTag,nodeCount)

			# Update Parent fields
			nodePack.addSplitType(nodeTag,rawTable[0].retrieve(splitFeature).fType)

			if rootNode == nodeTag:
				nodePack.addNodeType(nodeTag,NodeType.ROOT)
			else:
				nodePack.addNodeType(nodeTag,NodeType.UNDEF)

			nodePack.addSplitAtribute(nodeTag,splitFeature)
			nodePack.addSplitValue(nodeTag, splitValue)

	nodePack.switchNodeTypes(NodeType.EDGE,NodeType.LEAF)

	nodePack.updateMajority(rawTable)
	return nodePack



###############################################################################################

# if __name__ == '__main__':
# 	l = importDataCSV('metadata.csv','dummy.csv')
# 	a = InitTree(l)
