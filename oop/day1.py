'''
    -class:
        it is collection of function and variables which can
        work independently on its own

    -object:
        it is insatnce of class

'''

# class Animal:
#     def what_sound_does_it_make(self,flag):
#         if flag.lower() == 'bark':
#             print(f'Hey its a dog')
#         elif flag.lower() == 'meow':
#             print(f'Hey its a cat')
#         else:
#             print(f'Hey its a human')

# species_1 = Animal()
# species_1.what_sound_does_it_make('bark')

# species_2 = Animal()
# species_2.what_sound_does_it_make('meow')

# species_3 = Animal()
# species_3.what_sound_does_it_make('talks')

'''
    Task 
        create a class Calculator that must have following methods
        add2numbers subtract multiply and divide and run those methods
'''

class Calculator:
    def add(self,a,b):
        print( a+b )
    def sub(self,a,b):
        print( a-b )
    def multiply(self,a,b):
        print( a*b )
    def divide(self,a,b):
        print( a/b )
        
    #if it is required to run only in this instance
    if __name__ == '__main__': 
        print(f'{add(4+5)}')


# instance = Calculator()

# instance.add(2,2)
# instance.sub(2,2)
# instance.multiply(2,2)
# instance.divide(2,2)


'''
    how does encaptulation and different instances work!!
'''

# class Animal:
#     def __init__ (self,name,species,dob):
#         self.name = name
#         self.species = species
#         self.dob = dob

# species = Animal('rojo','dog','2015-5-3')
# species2 = Animal('jojo','cat','2022-5-3')
# print(species.name,species.species,species.dob)
# print('--'*25)
# print(species2.name,species2.species,species2.dob)

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

class User:
    def __init__(self,username,password,phone,note):
        self.username = username
        self.password = password
        self.phone = phone
        self.note = note
    
    def register_user(self):
        self.username = input('Enter username:\t')
        self.password = input('Enter Password:\t')
        self.phone = int(input('Enter Phone number:\t'))

    def authentication(self,in_username,in_password):
        if (self.username == in_username) and (self.password == in_password):
            self.welcome(self)
        else:
            print(f'Invalid Credential')
    
    def welcome(self):
        print(f'Welcome!! {self.username}\nphone number:{self.phone}')
        while True:
            choice = int(input(f'1.Add note\n2. Exit\nEnter your choice:\t'))
            if(choice == 1):
                self.note = input('Enter your note(press [enter] to save):\n')
            else: 
                break
myuser = User('unknown','unknown',111,'unknown')
myuser.register_user()