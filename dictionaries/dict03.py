employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

resDict = dict.fromkeys(employees, defaults)
print(resDict)

print(resDict["Kelly"])