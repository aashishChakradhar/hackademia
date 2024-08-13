'''
    stores like in dictionary
    {
        'ram':
            {
                'maths' : 20,
                'science': 30,
            }
    }
'''

import json

toSave = {
    'student':['ram','shyam','hari','gita'],
    'marks':[10,20,30,40]
}

with open ('fileHandeling/database_json.json','w') as jsfw:
    json.dump(toSave,jsfw)

with open('fileHandeling/database_json.json','r') as jsfr:
    loadJson = json.load(jsfr)
print(loadJson)