# customer = {
#     "Name" : "John Smith",
#     "age" : 30,
#     "phone" : 1234567
# } #key value

# print(customer["Name"], customer["age"], customer["phone"])
# # print(customer["name"]) #error
# print(customer.get("name")) #get method:show none
# print(customer.get("name", "🙂"))

# customer["DOB"]="23 Jan 2000"
# print(customer["DOB"])
# print(customer["Name"], customer["age"], customer["phone"], customer["DOB"])

# if ("phone") in customer:
#     print("Yes, it is")

# x, y, z = 3, 4, 5
# print(x+y+z)










# num = input("Enter Number : ")
# digit_map={
#     "1" : "One",
#     "2" : "Two",
#     "3" : "🙂"
# }

# output = ""
# for i in num:
#     output+=digit_map.get(i, "!")
# print(output)









# users = {
#     "admin" : "1234",
#     "student" : "abcd",
#     "teacher" : "pass123"
# }

# username = input("Enter username : ")
# password = input("Enter password : ")

# if username in users and users[username] == password:
#     print("Login Successful!")
# else:
#     print("Invalid username or password!")
    
    
    
    
    
    
    
# sentence = "pythin is easy and python is powerful"
# words = sentence.split() #split with space
# print(words)
# word_count = {}
    
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)   
    







# students = {}

# while True:
#     print("\n1. Add Student")
#     print("2. View Students")
#     print("3. Delete Student")
#     print("4. Exit")
    
#     choice = input("Enter choice: ")
    
#     if choice == "1":
#         name = input("Enter Name: ")
#         age = input("Enter age: ")
#         students[name] = age
        
#     elif choice == "2":
#         print(students)
        
#     elif choice == "3":
#         name = input("Enter name to delete: ")
#         if name in students:
#             del students[name]
        
#     elif choice == "4":
#         break
        
        
        
        
        
sales = {
    "Jan" : 1200,
    "Feb" : 1500,
    "Mar" : 1800,
    "Apr" : 900
}

highest = max(sales, key=sales.get)
lowest = min(sales, key=sales.get)
total = sum(sales.values())

#sales.get("Jan") -> 1200
#sales.get("Feb") -> 1500
#sales.get("Mar") -> 1800

print("Highest month:", highest)
print("Lowest month:", lowest)
print("Total sales:", total)
