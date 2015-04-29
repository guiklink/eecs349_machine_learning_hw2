# This file will contain all the functions that handle comunication with CSV file and data management


from data_util import *
import csv

################ CONVENTIONS #################
##############################################
#          Array of DataRow = table			 #
#            Data Row = Instance             #
##############################################

# IMPORT CSV DATA ##############################################################################

# Gets a string path for a CSV file and returns an array of DataRow (Table), where each position of the array
# will correpspond to a table line

# Entry -> (String) location of metadata.csv | (String) location of the CSV btrain.csv
# Returns -> array(DataRow) containing all data

def importDataCSV(metPath, dataPath):		
	metList = []
	dataList = []
	dataRowTable = []

	# Import and handle metadata.csv
	file = open(metPath)
	csvFile = csv.reader(file)
	for row in csvFile:
		metList.append(row)

	typeList = []
	for i in metList:
		typeList.append(i[1])
	typeList.pop(0)

	# Import and handle rawdata.csv
	file = open(dataPath)
	csvFile = csv.reader(file)
	for row in csvFile:
		dataList.append(row)

	tagList = dataList.pop(0)

	for row in dataList:
		dataRowTable.append(DataRow(tagList, row, typeList))

	return dataRowTable


###############################################################################################

# DATA FILTER #################################################################################

# Given a table, a feature and a value returns a table containing entries with that value

# Entry ->
# Returns ->

def filterTable(table, feature, value):		
	return 0

# OVERLOAD: Given a table, a feature and a value range returns a table containing entries with that value

def filterTable(table, feature, min, max):		
	return 0

###############################################################################################

