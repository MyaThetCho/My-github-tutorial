# # variable from main program = Global Variable
# # variable from sub program = Local Variable

# def Greeting(n): # n = parameter
#     print("Hi!!", n)

# def summation(n1, n2):
#     return n1+n2
    

# name = input("Enter name: ")  
# Greeting(name) # name = argument

# math = int(input("Enter math mark: "))
# eng = int(input("Enter eng mark: "))
# total = summation(math, eng)
# print("Avg :", total/2)



def add(n1, n2):
    print("The result", n1+n2)

def minus(n1, n2):
    print("The result", n1-n2)
    
def multi(n1, n2):
    print("The result", n1*n2)

def divi(n1, n2):
    print("The result", n1/n2)
    

num1 = "Enter first number: "
num2 = "Enter second number: "
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divsion")
    
    choice = input("Enter you choice : ")
    
    if choice == "1":
        add(num1, num2)
    
    elif choice == "2":
        add(num1, num2)



