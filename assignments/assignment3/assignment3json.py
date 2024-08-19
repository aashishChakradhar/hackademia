'''
Task 2: 
    WAP that uses oop
    has class user
    when initalized it provides options: 
    1. Sign up 
    2. Sign in 

    if 1 is pressed it redirects to a method named Register_User
    this method takes in username, password and mobile number

    if 2 is pressed it redirects to a method name authentication
    this method checks input username and password with self.username
    and self.password 

    if match it redirects to another method named welcome_user

    welcome user method greets them,displays username and displays 
    their mobile number

    also this method gives 3 options. 
    1. enter note 
    2. Display notes
    3. exit 

    if 1 is pressed user can input a large note that is saved for that 
    object 

    if 2 is pressed display the note that was saved earlier 

    if 3 is pressed terminate 
'''

import json
import os

class User:
    def __init__(self):
        # initializing variables
        self.username = None
        self.password = None
        self.phone = None
        self.note = None
        self.json_content = {}
        self.user_details = {}
        
        # to create json file it doesnot exists
        try:
            with open ('assignment3/user_json.json','r') as json_read:
                self.json_content = json.load(json_read)
        except:
            with open ('assignment3/user_json.json','w') as json_write:
                json.dump({},json_write)
                pass
        
        # creating main menu 
        os.system('clear')
        while True:
            try:
                choice = int(input('1. Sign up\n2. Sign in\n3. Exit\nEnter choice:\t'))
                if choice == 1:
                    self.register_user() 
                elif choice == 2:
                    self.authentication()
                else:
                    break
            except Exception as e:
                os.system('clear')
                print(f'{e}')
                print(f'---'*25)
    

    def read_json(self):
        with open ('assignment3/user_json.json','r') as json_read:
            self.json_content = json.load(json_read)

    def write_json(self):
        with open ('assignment3/user_json.json','w') as json_write:
            json.dump(self.json_content,json_write)

    def set_details(self):
        self.user_details = {
            self.username:{
                'password':self.password,
                'phone':self.phone,
                'note':self.note,
            }
        }

    def add_note(self):
        for username, info in self.json_content.items():
            if self.username == username:
                info['note'] = self.note
        self.write_json()


    def register_user(self):
        try:
            os.system('clear')
            # user details form
            self.username = input('Enter Username:\t')
            self.password = input('Enter Password:\t')
            self.phone = int(input('Enter Phone:\t'))
            self.note = ' '

            self.set_details()
            self.read_json()
            self.json_content.update(self.user_details)
            self.write_json()
            os.system('clear')
            print(f'User Created Successfully')
            print(f'---'*25)           
        except Exception as e:
            os.system('clear')
            print(f'Could not register\n{e}')
            print('---'*25)
    
    def authentication(self):
        try:
            os.system('clear')
            in_username = input('Enter Username:\t')
            in_password = input('Enter Password:\t')
            user_found = False
            self.read_json()
            for username, info in self.json_content.items():
                if username == in_username:
                    if info['password'] == in_password:
                        self.username = username
                        self.password = info['password']
                        self.phone = info['phone']
                        self.note = info['note']
                        self.set_details()
                        self.welcome_user()
                    else:
                        os.system('clear')
                        print(f'Incorrect Password!!')
                        print('---'*25)
                    user_found = True
            if not user_found:
                os.system('clear')
                print(f'User not found!!')
                print('---'*25)
        except Exception as e:
            os.system('clear')
            print(f'{e}')
            print('---'*25)
    
    def welcome_user(self):
        os.system('clear')
        while True:
            try:
                print(f'Welcome!!{self.username}\nPhone Number: {self.phone}')
                print('---'*25)
                choice = int(input(f'1. Enter note\n2. Display Notes\n3. Exit\nEnter your choice:\t'))
                os.system('clear')
                if choice == 1:
                    # taking note
                    self.note = self.note +' '+ input('Enter note:\n')
                    self.add_note()
                    os.system('clear')
                    print('Note added successfully!!')
                    print('---'*25)
                elif choice == 2:
                    os.system('clear')
                    print(f'Previous Note:\n{self.note}')
                    print('---'*25)
                else:
                    break
            except Exception as e:
                os.system('clear')
                print(f'{e}')
                print('---'*25)

user_operation = User()