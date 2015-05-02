import matplotlib.pyplot as plt
from model_validate import validateTree
import tree_util
from tree_gen import InitTree
import random
import csv
from csv_handler import importDataCSV
import math


trainData = importDataCSV("metadata.csv","dummy.csv")
valData = importDataCSV("metadata.csv", "dummy.csv")


def genCurve(trainData, valData):
	x = [] # stores the x axis of the graph
	trainList = [] # the list of accuracies derived from training data
	valList = [] # the list of accuracies derived from validation data
	i = 0
	while i < 1: 
		i = i+0.1
		a = 0
		b = 0
		# for trial in range(3):
		newData = sortData(trainData, i) #
		tree = InitTree(newData) # NEED TO GET THIS FUNCTION WHEN TREEGEN WORKS
		print "finished a tree"
		a = a + validateTree(tree, newData)
		print ""
		b = b + validateTree(tree, valData)
		# a = float(a)/3
		# b = float(b)/3
		# print "a: ", a, "b: ", b
		trainList.append(a)
		print "trainList: ", trainList
		valList.append(b)
		print "valList: ", valList
		x.append(i)

	plt.plot(x, trainList)
	plt.plot(x, valList)
	plt.xlabel('percent training used')
	plt.ylabel('percent accuracy')
	plt.title('learning curve')
	plt.show()


def sortData(dataSet, i):
	totData = len(dataSet)
	numData = int(math.ceil(i*totData))
	randomList = random.sample(xrange(totData), numData)
	newData = []
	for i in randomList:
		newData.append(dataSet[i])
	return newData
