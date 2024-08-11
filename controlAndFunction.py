"""
conditional statements
"""
# x = True
# if x:{
# print("hello")
# }
# else:{
#     print("bye")
# }

# x = 1
# print(f"{x, type(x)}")
# if x%2==0:
#     print(f"Even")
# if x%2 != 0:
#     print(f"odd")

# username = input("Enter username: ")
# password = input("Enter password: ")
# print(f"Welcome {username}") if username == 'admin' and password == 'admin' else print(f"Invalid")

#kbc
# score = 0
# kbc = {
#     "question1":{
#         "where was buddha born?":"nepal"
#     },
#     "question2":{
#         "what is the height of mt everest?":"8848",
#     },
#     "question3":{
#         "who is current prime minister of nepal?":"kp oli",
#     },        
# }
# for num,questions in kbc.items():
#     for question,answer in questions.items():
#         print(f"{question}")
#         ans1 = input(" ").lower()
#         if answer == ans1:
#             score += 10
#         else:
#             print(f"wrong answer.\nscore: {score}")
# print(f"Total score: {score}")

# # recursion function
# def factorial (n):
#     if n ==0 or n ==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(3))

# #task 7 add num using recursion
def recursion(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n +recursion(n-1)
print(recursion(5))

#task 8 reverse a string using recursion
def revString(word):
    n = len(word)-1
    if(n == 0):
        return ""
    else:
        print(word[n])
        return word[n]+revString(word[n-1])
print(revString('happy'))
