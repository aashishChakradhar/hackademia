''''
- all variables are volatile 
- for long time use we can storethese variables permanently
in a file
'''
# userName = input('Enter username: ')
# password = input('Enter password: ')
# print(userName,password)

# writting in file
with open ('fileHandeling/database.txt ','a+') as f:
    fromFile = f.readlines()
print (fromFile)

# task 2
'''
write a note
read a note
if 1 to write
if 2 read

'''
# while True:
#     choice = int(input('1. Write note\n2. Read note\n 0. Exit\nEnter your choice: '))
#     if choice == 1:
#         note = input('enter note:\n')
#         with open ('fileHandeling/database.txt ','a') as f:
#             f.writelines(note + '\n')
#     elif choice ==2:
#         with open ('fileHandeling/database.txt ','r') as f:
#             outputFile = f.readlines()
#         print(outputFile)
#     else:
#         break

'''
task 3
1. signup
2. sign in

1 is pressed
    username, password, mobile number
2 is pressed
    read username and password and check with db
'''

while True:
    choice = int(input('1. Signin\n2. Signup\n 0. Exit\nEnter your choice: '))
    if choice == 1:
        username = input('username:\n')
        password = input('password:\n')
        phone = input('phone:\n')
        with open ('fileHandeling/database.txt ','a') as f:
            f.writelines(username +' '+ password +' '+ phone +'\n')
    elif choice ==2:
        with open ('fileHandeling/database.txt ','r') as f:
            outputFile = f.readlines()
            for sp in outputFile:
                detail = sp.split
                if detail[0] == username and detail[1] == password:
                    print(f'{detail[2]}') 
                else:
                    print('Invalid Details')
                    break
        print(outputFile)
    else:
        break
