'''
    exception or error handeling!!!
    -
    try:
        code in try block code that is to be executed
    except:
        if code fails rest of the part runs here
'''

# # example
# while True:
#     x = int(input('Enter numberator'))
#     y = int(input('Enter denominator'))
#     try:
#         output = x/y
#         print(output)
#     except Exception as e:
#         print('got an error')
#         break



'''
start infinite loop
get random numberator and denominator,
calculate total number of crashes
if crashes == 100 break the program
'''

import random
count = 0
while True:
    a = random.randrange(0,100)
    b = random.randrange(0,100)
    try:
        output = a/b
    except:
        count += 1
        print(f'Crash count: {count}')
        if(count == 100):
            break
print(f'Total number of crashes: {count}')

