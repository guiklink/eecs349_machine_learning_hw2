# This file will contain all the functions that handle comunication with CSV file and data management


from data_util import *


################ CONVENTIONS #################
##############################################
#          Array of DataRow = table			 #
##############################################

# IMPORT CSV DATA ##############################################################################

# Gets a string path for a CSV file and returns an array of DataRow (Table), where each position of the array
# will correpspond to a table line

def importDataCSV(path):		
	return 0


###############################################################################################

# DATA FILTER #################################################################################

# Given a table, a feature and a value returns a table containing entries with that value

def filterTable(table, feature, value):		
	return 0

# OVERLOAD: Given a table, a feature and a value range returns a table containing entries with that value

def filterTable(table, feature, min, max):		
	return 0

###############################################################################################

