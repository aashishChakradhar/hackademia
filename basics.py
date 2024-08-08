# print("hello world")

"""
x = int(input('Enter number 1:'))
y=int(input('Enter number 2:'))
print(f'add:{x+y}\nsub:{x-y}\nmult:{x*y}\ndiv:{x/y}')
"""

# WAP to take principal, tile and rate then calculate the simple interest
P = float(input('Enter principal:'))
T = int(input('Enter time: '))
R = float(input('Enter Rate: '))
SI=(P*T*R)/100
print(f"PRINCIPLE:RS.{P}\nTIME:{T} YEARS\nRATE:{R}%\nSIMPLE INTEREST:RS.{SI}")
