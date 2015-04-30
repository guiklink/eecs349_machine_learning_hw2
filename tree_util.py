# This file contains the the alghorithm for J48


# Node ######################################################################################

class Node():
	def __init__(self, tag, parent, DataRowID, children, splitType, value, attribute):
		self.tag = tag
		self.parent = parent
		self.DataRowID = DataRowID
		self.children = children
		self.splitType = splitType
		self.value = value
		self.attribute = attribute

		### Add self.max and self.min for logic rules???

		phi = 0.1 #??????? COME BACK TO THIS

		def isLeaf(self):
			if NodeEntropy(self.tag) < phi  # If split is pure enough
				leaf = 1		# mark node as leaf to prevent further spliting
			else leaf = 0		# mark node as non-leaf for further splitting

			return leaf

		
###############################################################################################


# BEST SPLIT ##################################################################################

# Def

# Entry ->
# Returns ->

def BestSplit():		
	return 0


###############################################################################################

# NODE ENTROPY ####################################################################################

# Def

# Entry ->
# Returns ->

def NodeEntropy(tag):
	Nm = filterTableByID(table, idList, )	

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


# Retrieve Node ##############################################################################

# Function that returns a single node

# Entry -> DataRow[]
# Returns -> 

def RetrieveNode():	
	pass
		
	for row in table:
		print row.toStringCSV()

##############################################################################################
