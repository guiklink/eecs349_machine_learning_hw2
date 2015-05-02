# This file outputs the rules generated by the decision tree in Disjunctive Normal Form. 
from tree_util import *
from data_util import *


def getRules(tree):
	stop = len(tree.fields[tree.nType].keys())
	count = 0
	#for all of the nodes in tree model
	for i in tree.fields[tree.nType].keys():
		count+=1
		# find a leaf
		if NodeType.LEAF == tree.getNodeType(i):
			node = i #node=leaf.node
			Rule= "IF " 
			leafClass = tree.getMajorityClassification(node)
			
			while tree.getParent(node):

				splitVal = tree.getSplitValue(tree.getParent(node))
				splitAttribute = tree.getSplitAtribute(tree.getParent(node))
				if FeatureType.CONTINUOUS == tree.getSplitType(tree.getParent(node)):
					
					if node == tree.getChild0(tree.getParent(node)): 
						
						Rule = Rule + splitAttribute + " < " + str(splitVal)
						node = tree.getParent(node)
						if tree.getParent(node):
							Rule = Rule + " AND "
								
													
					else:
						Rule = Rule +splitAttribute + " >= " + str(splitVal)
						node = tree.getParent(node)
						if tree.getParent(node):
							Rule = Rule + " AND "
						
				elif FeatureType.DISCRETE == tree.getSplitType(tree.getParent(node)):
					
					if node == tree.getChild0(tree.getParent(node)): 

						Rule = Rule +splitAttribute + " != " + str(splitVal)
						node = tree.getParent(node)
						if tree.getParent(node):
							Rule = Rule + " AND "
						
					else:
						Rule = Rule +splitAttribute + " = " + str(splitVal)
						node = tree.getParent(node)
						if tree.getParent(node):
							Rule = Rule + " AND "
		
			if leafClass > 0: 
				print Rule
				print tree.getNodeType(node)
				if NodeType.ROOT == tree.getNodeType(node):
					print " THEN WINNER."
				if count != stop:
					print "OR"
			else:
				print Rule
				if NodeType.ROOT == tree.getNodeType(node):
					print " THEN LOSER."
				if count != stop:
					print "OR"
