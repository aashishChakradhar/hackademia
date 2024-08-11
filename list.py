'''
list
- list is a collection of datatype that is capable of holding more than 1 variable
- its very similar to array but has 2 functional difference
- it is heterogenous for these you can put in any type of valuef (any datatypes)
- it is denoted with '[]' brackets
- each value has index or location associated 
'''
mylist = ['happy','apple',1,2.3]
# print(f"{mylist}")
# print(f"{len(mylist)}")
# print(f"{type(mylist)}")

# #iterating over list using index value
# for i in range(len(mylist)):
#     print(f"{mylist[i]}")

# # interating over list using element itself
# for i in mylist:
#     print(i)

# # finding index of list
# for list_index,list_element in enumerate(mylist):
#     print(f'{list_index,list_element}')

# # print only even number
# numList = [1,2,3,4,5,6,7,8,9]
# for x in numList:
#     print(f'{x} is even') if(x % 2 ==0) else print(f"{x} is odd")

# # adding elements in list
# print(f'{mylist}')
# print(f'{len(mylist)}')
# mylist.append('hello')
# print(f'{mylist}')

# task create list that contain even number form 1 to 100

evenNum = []
for x in range(100):
    if x % 2 == 0:
        evenNum.append(x)
print(f"{evenNum}")
