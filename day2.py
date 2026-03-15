# num = int(input("Enter number : "))
# if num > 0:
#     print("Positive number")
# elif num<0:
#     print("Negative number")
# else:
#     print("Zero")


# num1 = (input("Enter number 1 : "))
# num2 = (input("Enter number 2 : "))
# num3 = (input("Enter number 3 : "))
# if num1 > num2:
#     if num1 > num3:
#         print(num1)
#     else:
#         print(num3)
# elif num2 > num3:
#     print(num2)
# else:
#     print(num3)


# postcode = input("Enter postcode : ")
# length = len(postcode)
# if length>=6 and length<=8:
#     print("Valid")
# else:
#     print("Invalid")

# password = input("Enter password : ")
# if len(password)<6:
#     print("The password you have entered is not long enough")
# else:
#     print("Length of password OK")


# text ="Computer Science"
# print(text[0:3])
# print(text[0])
# print(text[-2])
# print(text[:5])
# print(text[1:-1])

# first_name = input("Enter first name : ")
# last_name = input("Enter last name : ")

# if len(last_name)>=4:
#    print(last_name[0:4] + first_name[0].upper())
# else:
#     print(last_name + (4-len(last_name)) * "X" + first_name[0].upper())


age = int(input("Enter your age : "))
if age>18:
    print(f"You need to take {((age-18) * 2) + 20} lessons")
else:
    print("You need to take 20 lessons")
