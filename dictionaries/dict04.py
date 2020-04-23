sampleDict = {'name': 'Kelly', 'age': '25', 'salary': 8000, 'city': 'New york'}

newDict = dict()
for item in ['name', 'salary']:
	newDict[item] = sampleDict[item]

print(newDict)