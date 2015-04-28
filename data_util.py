# This file contains all the data structures for data

# FEATURES TYPE #################################################################################

from enum import Enum 					# If your python version doesn't support enum in linux open a terminal and execute "sudo pip install enum34"
class FeatureType(Enum):				# Enumerator for types of data 
	DISCRETE = 0						
	CONTINUOUS = 1 

#################################################################################################


# FEATURES ######################################################################################

class Feature():
	def __init__(self, tag, value, fType):
		self.tag = tag								# Name of the feature (helps debuging)
		self.value = value 							# Value for the feature
		self.fType = fType							# Type of data stored 

	def getValue(self):								# return the value converted to the apropriate type (use this function to retrieve the feature value)
		if self.fType == FeatureType.DISCRETE:
			return str(self.value)
		elif self.fType == FeatureType.CONTINUOUS:
			return float(self.value)

		
###############################################################################################

# DATA ROW ####################################################################################

class DataRow():											# Data structure for a row of data 
	def __init__(self, id, tagList, valueList, typeList):
		self.id = id										# Unique id of the line (help debugging)
		self.nFeatures = len(valueList)						# Total number of features per row

		self.features = []									# Creates an array of datatype Feature

		for i in range(self.nFeatures):								# Iterates to each element of the lists provided
			tmp = Feature(tagList[i], valueList[i], typeList[i])	# Create a Feature datatype
			self.features.append(tmp)								# Stores feature in the array


###############################################################################################