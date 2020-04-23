sampleDict = {
	'physics': 82,
	'math': 65,
	'history': 75
}

myList = list()

myList = sorted(zip(sampleDict.values(), sampleDict.keys()))

print(myList)

minKey = min(myList)

print(minKey[1])

