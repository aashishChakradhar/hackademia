mydict = {
    'one':'hello',
    'two':'world',
}
print(f'type of :{type(mydict)}')
print(f'keys: {mydict.keys()}')
print(f'values: {mydict.values()}')
print(f'dictionary: {mydict}')
print(f'items: {mydict.items()}')

# modifying using list
listKeys = ['apple','ball','cat']
listValues = ['fruit','object','animal']
newDict = dict(zip(listKeys,listValues))
print(f'{newDict}')

#update in dictionary
newDict.update({'hello':'world'})
print(f'{newDict}')

# #task quiz question answer using zip 
# question = []
# answer = []
# num = int(input('Enter number of question: '))
# for i in range(num):
#     question.append(input(f"question {i+1}: "))
#     answer.append(input(f"answer {i+1}: "))
# questionDictionary = dict(zip(question,answer))
# print(f'{questionDictionary}')