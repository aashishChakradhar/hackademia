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
class User:
    def __init__(self):
        # initializing variables
        self.username = None
        self.password = None
        self.phone = None
        self.note = None
        
        # to create json file it doesnot exists
        try:
            with open ('assignments/user_json.json','r'):
                pass
        except:
            with open ('assignments/user_json.json','w'):
                pass
        
        # creating main menu 
        while True:
            choice = int(input('1. Sign up\n2. Sign in\n3. Exit\nEnter choice:\t'))
            if choice == 1:
                self.register_user() 
            elif choice == 2:
                self.authentication()
            else:
                break
    
    def register_user(self):
        # user details form
        self.username = input('Enter Username:\t')
        self.password = input('Enter Password:\t')
        self.phone = input('Enter Phone:\t')
        self.note = ' '

        # writing to the json file
        try:
            with open('assignments/user_json.json','r') as json_read:
                details = json.load(json_read)
            details.update({
                self.username:{
                    'password': self.password,
                    'phone': self.phone,
                    'note':self.note,
                }
            })
            with open ('assignments/user_json.json','w') as json_write:
                json.dump(details,json_write)
                
        except:
            print(f'Could not register')
    
    def authentication(self):
        # intake user credentials
        in_username = input('Enter Username:\t')
        in_password = input('Enter Password:\t')
        user_found = False

        # reading details form json file
        with open ('assignments/user_json.json','r') as json_detail:
            user_details = json.load(json_detail)

        for username, details in user_details.items():
            if username == in_username:
                if details['password'] == in_password:
                    self.username = username
                    self.password = details['password']
                    self.phone = details['phone']
                    self.note = details['note']
                    self.welcome_user()
                else:
                    print(f'Incorrect Password!!')
                user_found = True
        if not user_found:
            print(f'User not found!!')
    
    def welcome_user(self):
        print(f'Welcome!!{self.username}\nPhone Number: {self.phone}')
        print('--'*25)
        while True:
            choice = int(input(f'1.Enter note\n2. Display Notes\n3. Exit\nEnter your choice:\t'))
            if choice == 1:
                # taking note
                self.note = self.note +' '+ input('Enter note:\n')
                
                # writing to a file
                with open('assignments/user_json.json','r') as json_details:
                    user_details = json.load(json_details)
                for username, details in user_details.items():
                    if username == self.username:
                        print(type(details))
                        details.update({'note':self.note})
                
                with open('assignments/user_json.json','w') as json_write:
                    json.dump(user_details,json_write)
                
            elif choice == 2:
                print(f'Previous Note: {self.note}')
            else:
                break

user_operation = User()