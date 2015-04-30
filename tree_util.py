# This file contains the the alghorithm for J48

# Importing...

from csv_handler import *
from math import log

# NODE TYPE #################################################################################

from enum import Enum 					# If your python version doesn't support enum in linux open a terminal and execute "sudo pip install enum34"
class NodeType(Enum):				# Enumerator for types of data 
	ROOT = 0						
	EDGE = 1
	LEAF = 2
	UNDEF = 3 			

#################################################################################################

# Node ######################################################################################

class NodePack():
	def __init__(self):
		self.fields = [{},{},{},{},{},{}]
		self.parent = 0
		self.child0 = 1
		self.child1 = 2
		self.splitType = 3
		self.nType = 4
		self.dataRowIDs = 5
	
	def addNode(self, tag):
		for i in range(len(self.fields)):
			self.fields[i].update({tag:None})
		
	def removeNode(self, tag):
		for i in range(len(self.fields)):
			del self.fields[i][tag]	

	def addParent(self, tag, parent):
		self.fields[self.parent].update({tag:parent})

	def removeParent(self, tag):
		self.fields[self.parent].update({tag:None})

	def getParent(self, tag):
		return self.fields[self.parent][tag]

	def addChild0(self, tag, child0):
		self.fields[self.child0].update({tag:child0})

	def removeChild0(self, tag):
		self.fields[self.child0].update({tag:None})

	def getChild0(self, tag):
		return self.fields[self.child0][tag]

	def addChild1(self, tag, child1):
		self.fields[self.child1].update({tag:child1})

	def removeChild1(self, tag):
		self.fields[self.child1].update({tag:None})

	def getChild1(self, tag):
		return self.fields[self.child1][tag]

	def addSplitType(self, tag, splitType):
		self.fields[self.splitType].update({tag:splitType})

	def removeSplitType(self, tag):
		self.fields[self.splitType].update({tag:None})

	def getSplitType(self, tag):
		return self.fields[self.splitType][tag]

	def addNodeType(self, tag, nodeType):
		self.fields[self.nodeType].update({tag:nodeType})

	def removeNodeType(self, tag):
		self.fields[self.nodeType].update({tag:None})

	def getNodeType(self, tag):
		return self.fields[self.nodeType][tag]

	def addDataRowIDs(self, tag, dataRowIDs):
		self.fields[self.dataRowIDs].update({tag:dataRowIDs})

	def removeDataRowIDs(self, tag):
		self.fields[self.dataRowIDs].update({tag:None})

	def getDataRowIDs(self, tag):
		return self.fields[self.dataRowIDs][tag]

	def getNodeEntropy(self, tag, csvData):
		if self.getDataRowIDs(tag) == None:							# test if DataRows was initialized if not return an error
			raise NameError('This node links to no instance!')
		nm = filterTableByID(csvData, self.getDataRowIDs(tag))
		if len(nm) == 0:											# checks if the instances for the node were found
			raise NameError('The IDs in your node dont match any node in the raw data!')

		classifierTag = nm[0].retrieveClassifierTag()				# takes the classifier from the 1th data row
		entropy = 0													# init a variable to store entrophy
		classValues = distinctAtributes(nm,classifierTag)			# retrieve all possible classifier values
		for val in classValues:
			pct = atributePct(nm,classifierTag,val)					# gets the % of that value in the whole data
			entropy += pct * log(pct,2)								# calculates and store entropy for the value
		return (-1 * entropy)										# return entrophy

	def getSplitEntropy(self, featureTag, value):
		pass
		
###############################################################################################


# BEST SPLIT ##################################################################################

# Def

# Entry ->
# Returns ->

def BestSplit():		
	return 0


###############################################################################################

# ENTROPHY ####################################################################################

# Def

# Entry ->
# Returns ->

def BestSplit():		
	return 0


###############################################################################################

# SPLIT ENTROPHY ##############################################################################

# Def

# Entry ->
# Returns ->

def SplitEntrophy():		
	return 0

# Overload for multiple values

###############################################################################################



