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
# list a=[1,2,3,4,5] create b such that it has square of a
a=[1,2,3,4,5]
b =[]
for i in a:
    b.append(i**2)
print('--'*25)
print(b)
print('--'*25)
c = [i**2 for i in a]
print(c)