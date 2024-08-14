'''
    1. List Comprehension and generator expression
        list comprehension are a consise way to create list in python
        they are faster than using a for loop to create a list.
'''
# example
# oddNumbers = [i for i in range(1,100,2)]
# print(oddNumbers)

'''
    list comprehension works well when working with simple data
'''
# # list a=[1,2,3,4,5] create b such that it has square of a
# a=[1,2,3,4,5]
# b =[]
# for i in a:
#     b.append(i**2)
# print('--'*25)
# print(b)
# print('--'*25)
# c = [i**2 for i in a]
# print(c)

'''
square if even and cube if odd
'''
even = [i**2 if i%2==0 else i**3 for i in range(1,100)]
print(even)

'''
    Generator in python:
        -special type of function that returns a multiple value
        for multiple different instances using yield
        -gives new value everytime it is accessed


    example:
    def function_name():
        yield statement
'''

# Simple Generator
def simpleGenerator():
    yield 'a'
    yield 'b'
    yield 'c'

# first approach in gettin result from generator function
for value in simpleGenerator():
    print(value)
print('--'*25)
x = simpleGenerator()
print(type(x))
print(next(x))
print(next(x))
# print(next(x))
# print(next(x))

# Generator Expression
'''
    create genrator object vary similar to list comprehension
'''
square_gen = (x**2 for x in range(10))
print(square_gen)
print(list(square_gen))


'''
    Create a generator operator that yeilds all the even number
    using generator expression
    create an infinite loop where user is asked to type something 
    if the user types next
    display the next value of the generator operator
    when the iteration is over the loop must exit(hint: Using try except to handel this situation)
'''

# taskGenerator = ( x for x in range (2,10,2))
# while True:
#     userInput = input('Enter any thing: ')
#     try:
#         if(userInput == 'next'):
#             print(next(taskGenerator))
#         else:
#             print(taskGenerator)
#     except:
#         print('exiting')
#         break

'''
    Lambda function:
        - Lambda are often refered as annonymous function
        - For very short operations
        - these function are used in conjunction with higher level functions like map, filter, so on
'''
print('--'*25)
parameter = 2
x = lambda parameter : parameter **2
print(type(x))
print(x)

print('--'*25)
parameter1 = 2
parameter2 = 2
sumOfNumber = (lambda parameter1, parameter2: parameter1+parameter2)
print((sumOfNumber))


'''
    Task 2, given list_1 = [1,2,3,4,5,6,7,8,9,10] create lambda function that returns half
    of that value and pass each element of this list  to that function and save everything
    in new list (using list comprehension)
'''
print('--'*25)
list_1 = [x for x in range(10)]
half = lambda elem : elem/ 2
newList = [half(element) for element in list_1]

print(list_1)
print(newList)

'''
    WAP to take N (N = number of elements on a lis)
    loop till N times and get different numbers
    put all the numbers in a list named list_variables
    create lambda fuction that takes in parameter1 return even or odd
    using list comprehension create another list name odd_even_list it should contain all the output of t
        lambda function passed over each element of list_variable
    create dataframe with 2 columbs, number, even/odd
    number columb should have list variable on it and even/odd column should have odd_even_lis
    dispal final dataframe
'''
print('--'*25)
N = int(input('Enter number of element of list: '))
list_variables = []
for loop in range(N):
    list_variables.append ( int(input(f'element {loop} : ')))

check = lambda parameter1 : 'even' if parameter1 % 2 == 0 else 'odd'

odd_even_list = [check(x) for x in list_variables]
dict_input = {'number':list_variables,
              'odd/even':check}
import pandas as pd 
task_dataframe = pd.DataFrame(dict_input)
print(task_dataframe)

