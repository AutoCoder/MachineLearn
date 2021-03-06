def loadDataSet():
	postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'], \
					['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],\
					['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'], \
					['stop', 'posting', 'stupid', 'worthless', 'garbage'], \
					['mr', 'licks', 'ate', 'my', 'steak', 'how','to', 'stop', 'him'],\
					['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
					]
	classVec = [0,1,0,1,0,1]
	return postingList,classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWords2Vec(VocabList, inputSet):
	returnVec = [0]*len(VocabList)
	for word in inputSet:
		if word in VocabList:
			returnVec[VocabList.index(word)] = 1
		else:
			print "the word: %s is not in my Vocabulary!" % word
	return returnVec

def trainNB0(trainMatrix, trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs)
	p0Num = zeros(numWords); p1Num = zeros(numWords)
	p0Denom = 0.0; p1Denom = 0.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = p1Num/p1Denom
	p0Vect = p0Num/p0Denom
	return p0Vect,p1Vect,pAbusive


if __name__ == '__main__':
	from numpy import *
	ListOPosts,listClasses = loadDataSet()
	VocabList = createVocabList(ListOPosts)
	#print VocabList
	#print setOfWords2Vec(VocabList, ListOPosts[0])
	trainMat = []
	for postinDoc in ListOPosts:
		trainMat.append(setOfWords2Vec(VocabList,postinDoc))
	p0V,p1V,pAb = trainNB0(trainMat, listClasses)
	print p0V
	print p1V
	print pAb