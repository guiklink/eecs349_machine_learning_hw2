# This file contains all the data structures for data

# FEATURES TYPE #################################################################################

from enum import Enum 					# If your python version doesn't support enum in linux open a terminal and execute "sudo pip install enum34"
class FeatureType(Enum):				# Enumerator for types of data 
	DISCRETE = 0						
	CONTINUOUS = 1 

def stringToEnum(fType):					# Converts string to enum type
	if fType == "discrete":
		return FeatureType.DISCRETE
	if fType == "continuous":
		return FeatureType.CONTINUOUS				

#################################################################################################


# FEATURES ######################################################################################

class Feature():
	def __init__(self, tag, value, fType):
		self.tag = tag.strip()								# Name of the feature (helps debuging) | .strip() trims blanks e.g. " "
		self.value = value.strip() 							# Value for the feature | .strip() trims blanks e.g. " "
		self.fType = stringToEnum(fType.strip())			# Type of data stored converted to ENUM FeatureType | .strip() trims blanks e.g. " "

	def getValue(self):								# return the value converted to the apropriate type (use this function to retrieve the feature value)
		if self.fType == FeatureType.DISCRETE:
			val = str(self.value)
		elif self.fType == FeatureType.CONTINUOUS:
			if(self.value == "?"):						# replace '?' for None(null)
				val = None
			else:
				val = float(self.value)
		return val

	def toString(self):								# returns the Feature in a string format proper for printing
		return str(self.tag) + " | " + str(self.value) + " | " + str(self.fType)


###############################################################################################

# DATA ROW ####################################################################################

class DataRow():											# Data structure for a row of data 
	def __init__(self, tagList, valueList, typeList):
		self.id = valueList[0]								# Unique id of the line (help debugging)
		self.nFeatures = len(valueList)						# Total number of features per row
		self.features = []									# Creates an array of datatype Feature
		self.headers = (map(str.strip, tagList))[1:-1]		# An array holding the description of each feature

		for i in range(len(valueList)):								# Iterates to each element of the lists provided
			tmp = Feature(tagList[i], valueList[i], typeList[i])	# Create a Feature datatype
			self.features.append(tmp)								# Stores feature in the array

	def toString(self):										# returns the DataRow in a string format proper for terminal
		s = ""
		for f in self.features:
			s += " [" + f.toString() + "] "
		return s

	def toStringCSV(self):									# returns the DataRow in a string format proper for excel
		s = ""
		for f in self.features:
			s += str(f.value) + ","
		return s[0:-1]

	def toStringHeaders(self):								# returns a list of strings containing the tags of the features in the row
		s = ""
		for f in self.features:
			s += f.tag + ","
		return s[0:-1]

	def retrieve(self, tag):								# retrieve feature by tag
		for f in self.features:
			if f.tag == tag:								# if tag found return
				return f
		raise NameError('Trying to retrieve from an unexistent column!')	# if tag not found raise an error

	def retrieveClassifierTag(self):
		return self.features[self.nFeatures - 1].tag

###############################################################################################

# Table Printer ##############################################################################

# Function that prints on terminal a DataRow[]

# Entry -> DataRow[]
# Returns ->

def printTable(table):		
	for row in table:
		print row.toStringCSV()

###############################################################################################