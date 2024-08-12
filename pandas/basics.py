import pandas as pd
import numpy as np

dictionayVariables = {
    'student':['Ram','shyam','Sita','Geeta'],
    'marks':[10,20,30,40],
    
}
# creating a dataframe
data_frame_variable = pd.DataFrame(dictionayVariables)#converts dictionary into table/dataframe
print('Before adding new column: ')
print(data_frame_variable)

#adding new column
#create a list
data_frame_variable['social_skills']=[10,20,30,40]
print('after addibg social skills: ')
print(data_frame_variable)

# removing a column
data_frame_variable = data_frame_variable.drop(columns = 'social_skills')
print(f'after dropping a column:\n{data_frame_variable}')

# # get n number of question and ansewer from user
# num = int(input('Enter number of question:'))
# question_list = []
# answer_list = []
# question_dict = {}
# for x in range(num):
#     question_list = input(f'question {x+1}: ')
#     answer_list = input(f'answer {x+1}: ')
#     question_dict.append[question_list] = answer_list
# question_data_frame_variable = pd.DataFrame(question_dict)

#look up certain row:
print(data_frame_variable.loc[data_frame_variable['marks']<=20])

# tast 2

print('--'*25)
print('task 2')
data_frame_variable['question']=['hello','hi','yes','no']
print(data_frame_variable)
print(data_frame_variable.loc[data_frame_variable['question'] == "yes"])

print('--'*25)
# saving dataframe in csv file
data_frame_variable.to_csv('Data.csv',index = False)
# loading datafile
new_dataframe = pd.read_csv('Data.csv')
print('loaded from csv')
print(new_dataframe)
# read row
print('--'*25)
print(new_dataframe.iloc[1])