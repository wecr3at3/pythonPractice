sampleDict = {
	'name': 'Kelly',
	'age': 25,
	'salary': 8000,
	'city': 'New york'
}

keysToRemove = ['name', 'salary']
for item in keysToRemove:
	del sampleDict[item]

print(sampleDict)