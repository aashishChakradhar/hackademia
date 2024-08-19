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
import os
class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.phone = None
        self.note = None
        self.details = {}
        os.system('clear')
        while True:
            choice = int(input('1. Sign up\n2. Sign in\n3. Exit\nEnter your choice:\t'))
            if choice == 1:
                self.register_user()
            elif choice == 2:
                self.authentication()
            else:
                break
    
    def load_data(self):
        for username, info in self.details.items():
            if self.username == username:
                self.password = info['password']
                self.phone = info['phone']
                self.note = info['note']
                
        
    def register_user(self):
        os.system('clear')
        self.username = input('Enter Username:\t')
        self.password = input('Enter Password:\t')
        self.phone = int(input('Enter phone number:\t'))
        self.note = ''
        self.details.update({
            self.username:{
                'password' : self.password,
                'phone' : self.phone,
                'note' : self.note,
            }
        })
        os.system('clear')
        print(f'User Created SUccessfully')
        print('---'*25)
    
    def authentication(self):
        os.system('clear')
        user_found = False
        in_username = input('Enter Username:\t')
        in_password = input('Enter Password:\t')
        for username,info in self.details.items():
            if username == in_username :
                user_found = True
                if info['password'] == in_password:
                    self.username = username
                    self.load_data()
                    os.system('clear')
                    print('Login Successful')
                    print('---'*25)
                    self.welcome_user()
                else:
                    os.system('clear')
                    print('Invalid Password')
                    print('---'*25)
        if not user_found:
            os.system('clear')
            print('User not found')
            print('---'*25)

    def welcome_user(self):
        while True:
            print(f'Welcome {self.username}!!\nphone Number: {self.phone}\n')
            choice = int(input('1. Enter note\n2. Display note\n3. Exit\nEnte your choice:\t'))
            os.system('clear')
            if choice == 1:
                for username,info in self.details.items():
                    if self.username == username:
                        self.note += ' ' + input('Enter note:\n')
                        info.update({
                            'note':self.note
                        })
                os.system('clear')
                print('Note updated Successfully!!')
                print('---'*25)

            elif choice == 2:
                print(f'Your Note:\n{self.note}')
                print('---'*25)
            else:
                break

log = User()