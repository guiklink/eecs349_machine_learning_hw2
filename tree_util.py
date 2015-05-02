# This file contains the the alghorithm for J48

# Importing...

from csv_handler import *
from math import log
import numpy as np

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
		self.fields = [{},{},{},{},{},{},{},{}]
		self.parent = 0
		self.child0 = 1
		self.child1 = 2
		self.splitType = 3
		self.nType = 4
		self.dataRowIDs = 5
		self.splitAtribute = 6
		self.splitValue = 7
	
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
		self.fields[self.nType].update({tag:nodeType})

	def removeNodeType(self, tag):
		self.fields[self.nType].update({tag:None})

	def getNodeType(self, tag):
		return self.fields[self.nType][tag]

	def addDataRowIDs(self, tag, dataRowIDs):
		self.fields[self.dataRowIDs].update({tag:dataRowIDs})

	def removeDataRowIDs(self, tag):
		self.fields[self.dataRowIDs].update({tag:None})

	def getDataRowIDs(self, tag):
		return self.fields[self.dataRowIDs][tag]

	def addSplitAtribute(self, tag, splitAtribute):
		self.fields[self.splitAtribute].update({tag:splitAtribute})

	def removeSplitAtribute(self, tag):
		self.fields[self.splitAtribute].update({tag:None})

	def getSplitAtribute(self, tag):
		return self.fields[self.splitAtribute][tag]

	def addSplitValue(self, tag, splitValue):
		self.fields[self.splitValue].update({tag:splitValue})

	def removeSplitValue(self, tag):
		self.fields[self.splitValue].update({tag:None})

	def getSplitValue(self, tag):
		return self.fields[self.splitValue][tag]

	def retrieveListOfNodesByType(self, nType):
		result = []
		for n in self.fields[self.nType].keys():
			if self.fields[self.nType][n] == nType:
				result.append(n)

		return result 								# return a list of node tags

	def retrieveNodesByType(self, nType):
		result = []
		for nTag in self.fields[0].keys():
			if self.getNodeType(nTag) == nType:
				result.append(nTag)
		return result

	def printNodePack(self):
		for n in self.fields[0].keys():
			print '\n==> NODE: ' + str(n)
			print '=====> Type: ' + str(self.getNodeType(n))
			print '=====> Parent: ' + str(self.getParent(n))
			print '=====> Child0: ' + str(self.getChild0(n))
			print '=====> Child1: ' + str(self.getChild1(n))
			print '=====> Data Instances: ' + str(self.getDataRowIDs(n))
			print '=====> Split Atribute: ' + str(self.getSplitAtribute(n))
			print '=====> Split Value: ' + str(self.getSplitValue(n))

###############################################################################################

# ENTROPHY ####################################################################################

# Give back the entrophy of the node

# Entry -> String (NodeTag) | DataRow[] (The whole training data table)
# Returns -> Float (Entropy)

	def getNodeEntropy(self, tag, csvData):
		if self.getDataRowIDs(tag) == None:							# test if DataRows was initialized if not return an error
			raise NameError('This node links to no instance!')
		nm = filterTableByID(csvData, self.getDataRowIDs(tag))
		if len(nm) == 0:											# checks if the instances for the node were found
			print self.getDataRowIDs(tag)
			raise NameError('The IDs in your node dont match any node in the raw data!')

		classifierTag = nm[0].retrieveClassifierTag()				# takes the classifier from the 1th data row
		entropy = 0													# init a variable to store entrophy
		classValues = distinctAtributes(nm,classifierTag)			# retrieve all possible classifier values
		for val in classValues:
			pct = atributePct(nm,classifierTag,val)					# gets the % of that value in the whole data
			entropy += pct * log(pct,2)								# calculates and store entropy for the value
		return (-1 * entropy)										# return entrophy
###############################################################################################

# GET SPLIT ENTROPY ##################################################################################

# Calulate the entropy of each node possible value for spliting

# Entry -> String (node tag) | String (feature to plit) | String (value to split)
# Returns -> Float (entropy)

	def getSplitEntropy(self, nodeTag, featureTag, value, table):
		
		featureType = table[0].retrieve(featureTag).fType

		nm = table

		classifier = table[0].retrieveClassifierTag()

		nmj = []

		possibleClassifiers = distinctAtributes(nm, classifier)

		splitEntropy = 0

		for nBranch in range(2):							# binary split only

			if featureType == FeatureType.DISCRETE:
				nmj.append(filterTable(nm, featureTag, value, None, nBranch)) # LAST ARGUMENT must be a boolean
			elif featureType == FeatureType.CONTINUOUS:
				if(value == None):
					value = np.median(retrieveDataFromColumn(nm,featureTag))
				maxValue = retrieveMaxFromColumn(nm,featureTag)
				minValue = retrieveMinFromColumn(nm,featureTag)

				if(value == maxValue or value == minValue):
					return 400, [[],[]] # No information gain if children are empty
				nmj.append(filterTable(nm, featureTag, value, maxValue, nBranch)) # LAST ARGUMENT must be a boolean

			for classifierValues in possibleClassifiers:
				prob = atributePct(nmj[nBranch],classifier,classifierValues)
				if prob <= 0:
					probLog = 0
				else:
					probLog = log(prob,2)
				splitEntropy += (float(len(nmj[nBranch])) / len(nm)) * prob * probLog

		return -1 * splitEntropy, nmj

###############################################################################################

# BEST SPLIT ##################################################################################

# Calulate the best node where a split can be performed

# Entry -> Float (a constant) | DataRow[] (csv data)
# Returns -> String (tag of the node that will be slip)| String (atribute for spliting) | String or Floar (value for spliting)

	def bestSplit(self, maxEntropy, table, splitedDiscrete,splitedValue):
		minEnt = maxEntropy

		bestTag = None
		bestAtribute = None
		bestValue = None
		#entropy = 5000

		for nTag in self.retrieveListOfNodesByType(NodeType.EDGE):
			print ">> nTag = " + str(nTag) 
			nm = filterTableByID(table,self.getDataRowIDs(nTag))
			for atribute in table[0].headers:
				if atribute not in splitedDiscrete:
					#print "atribute = " + str(atribute)
					for value in distinctAtributes(table, atribute):
						if (atribute,value) not in splitedValue:
							#print "value = " + str(value)
							entropy, nmj = self.getSplitEntropy(nTag,atribute,value,table)  
							#print "entropy = " + str(entropy)
							if entropy < minEnt:
								bestTag = nTag
								bestAtribute = atribute
								bestValue = value
		print 'Entropy = ' + str(entropy)
		print bestTag
		print bestAtribute
		print bestValue
		return bestTag, bestAtribute, bestValue, nmj

###############################################################################################




