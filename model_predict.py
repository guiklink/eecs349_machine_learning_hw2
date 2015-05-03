# This is a program that predicts the label of the last column
# of a test set based on the model trained using model-train 
# and subsequently validated using model-validate

from tree_util import *
from data_util import *
import model_validate
from tree_gen import InitTree
import csv

trainData = importDataCSV("metadata.csv","dummy.csv")
# tree = InitTree(trainData)
testData = importDataCSV("metadata.csv","dummytest.csv")


def predict(tree, dataSet):
	"""Used for predicting the outcome of a prediction set using a tree model, returns predicted outcome"""

	count = 0 #used for tracking how many times we've correctly classified our data
	for index in range(len(dataSet)):
		dataPoint = dataSet[index]
		node = 0
		for i in tree.fields[tree.nType].keys():
			if NodeType.ROOT == tree.getNodeType(i):
				node = i #basically an index
				print "root node: ", node
				break
			#keep going down the tree until no children exist, then get output classification

		print "node type", tree.getNodeType(node)

		while tree.getNodeType(node) != NodeType.LEAF:
			splitVal = tree.getSplitValue(node)
			print "tree split value: ", splitVal
			splitAttribute = tree.getSplitAtribute(node)
			print "tree split attribute: ", splitAttribute
			val = dataPoint.retrieve(splitAttribute).getValue()
			if val == None:		
				val = np.median(retrieveDataFromColumn(dataSetlitAttribute))

			print "data point value for split attribute: ", val
			if FeatureType.CONTINUOUS == tree.getSplitType(node): 
				if val >= splitVal:
					node = tree.getChild0(node)
					print "node type", tree.getNodeType(node)
					print "greater than", "going to next node", node
				else:
					node = tree.getChild1(node)
					print "lesser than", "going to next node", node
					print "node type", tree.getNodeType(node)
			elif FeatureType.DISCRETE == tree.getSplitType(node):
				if val != splitVal:
					node = tree.getChild0(node)
					print "not equal", " going to next node", node
					print "node type", tree.getNodeType(node)
				else:
					node = tree.getChild1(node)
					print "equal", "goint to next node", node
					print "node type", tree.getNodeType(node)
		leafClass = tree.getMajorityClassification(node)
		print "leaf classification: ", leafClass
		leafAttribute = dataSet[0].retrieveClassifierTag()
		print "leaf attribute: ", leafAttribute
		
		# Need to fill the last column (which is the same column as leafAttribute) with the 
		# value of the leaf (i.e. classify as winner or not)
		dataPoint.retrieve(leafAttribute).addValue(leafClass)
		print "prediction is: ", dataPoint.retrieve(leafAttribute).getValue()

	createFileCSV(dataSet)
	return dataSet

def createFileCSV(table, path="./prediction"):	
	""" Used to generate a .csv file with predicted labels in the last column (replacing question marks inside the test set."""	
	if len(table) < 1:
		raise NameError('Empty Table!')
	else:
		file = open(path + '.csv', 'w+')

		file.write(table[0].toStringHeaders() + "\n")

		for row in table:
			file.write(row.toStringCSV() + '\n')
		file.close() 