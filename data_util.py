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
		self.tag = tag								# Name of the feature (helps debuging)
		self.value = value 							# Value for the feature
		self.fType = stringToEnum(fType)			# Type of data stored converted to ENUM FeatureType

	def getValue(self):								# return the value converted to the apropriate type (use this function to retrieve the feature value)
		if self.fType == FeatureType.DISCRETE:
			return str(self.value)
		elif self.fType == FeatureType.CONTINUOUS:
			return float(self.value)

	def toString(self):								# returns the Feature in a string format proper for printing
		return str(self.tag) + " | " + str(self.value) + " | " + str(self.fType)


###############################################################################################

# DATA ROW ####################################################################################

class DataRow():											# Data structure for a row of data 
	def __init__(self, tagList, valueList, typeList):
		self.id = valueList[0]								# Unique id of the line (help debugging)
		self.nFeatures = len(valueList) - 1					# Total number of features per row

		self.features = []									# Creates an array of datatype Feature

		for i in range(1,len(valueList)):							# Iterates to each element of the lists provided, ignoring the 1th element that will ALWAYS be the ID
			tmp = Feature(tagList[i], valueList[i], typeList[i])	# Create a Feature datatype
			self.features.append(tmp)								# Stores feature in the array

	def toString(self):										# returns the DataRow in a string format proper for terminal
		s = ""
		for f in self.features:
			s += " [" + f.toString() + "] "
		return ("ID:" + str(self.id) + " " + s)

	def toStringCSV(self):									# returns the DataRow in a string format proper for excel
		s = ""
		for f in self.features:
			s += "," + f.toString()
		return ("ID:" + str(self.id) + s)

###############################################################################################