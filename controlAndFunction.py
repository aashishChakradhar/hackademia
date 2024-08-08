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
score = 0
kbc = {
    "question1":{
        "where was buddha born?":"nepal"
    },
    "question2":{
        "what is the height of mt everest?":"8848",
    },
    "question3":{
        "who is current prime minister of nepal?":"kp oli",
    },        
}
for num,questions in kbc.items():
    for question,answer in questions.items():
        print(f"{question}")
        ans1 = input(" ").lower()
        if answer == ans1:
            score += 10
        else:
            print(f"wrong answer.\nscore: {score}")
print(f"Total score: {score}")