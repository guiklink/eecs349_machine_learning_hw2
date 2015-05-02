import matplotlib as plt
import model_validation
import random

def genCurve(dataSet, tree):
	x = [] # stores the x axis of the graph
	trainList = [] # the list of accuracies derived from training data
	valList = [] # the list of accuracies derived from validation data
	i = 0
	while i < 1: 
		i = i+0.1
		a = 0
		b = 0
		for trial in range(3):
			newData = sortData(dataSet, i) # MAKE THIS
			tree = getTree(newData) # NEED TO GET THIS FUNCTION WHEN TREEGEN WORKS
			a = a + model_validation.validateTree(tree, newData)
			b = b + model_validation.validateTree(tree, newData)
		a = float(a)/3
		b = float(b)/3

		trainList.append(a)
		valList.append(b)
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






