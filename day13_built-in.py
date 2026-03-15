#################### max function ########################################
# item = ["Apple", "Mango", "Banana", "Papaya", "Orange"]
# list = max(item, key=len)
# print(list)


# word = "jqrtsjkadozfiwescsjxamwke"
# print(max(word))


#################### Lambda function #######################################

# addition = lambda x, y: x + y
# result = addition(3, 5)
# print("Result:", result)


# num = int(input("Enter = "))
# result = lambda a: 1/a
# print(result(num))


# minium = lambda x,y : x if (x<y) else y
# print("The smaller number is :", minium(35,74))


# check_num = lambda x: "Number is greater than 5" if x>5 else "Number is not greater than 5"
# print(check_num(6))


# num = int(input("Enter: "))
# check_num = lambda x: "Number is greater than 5" if x>5 else "Number is not greater than 5"
# print(check_num(num))


# result = lambda x: "P" if x>0 else "N" if x<0 else "Zero"
# print(result(0))


################### list() function #################################################################################

# string_example = "Hello. World!"
# list_from_string = list(string_example)
# print("Original String:", string_example)
# print("List from String:", list_from_string)


# # Converting a tuple to a list
# tuple_example = (1, 2, 3, 4, 5)
# list_from_tuple = list(tuple_example)
# print("Original Tuple:", tuple_example)
# print("List from Tuple:", list_from_tuple)


# # Creating a list from a range
# range_example = range(1, 6)
# list_from_range = list(range_example)
# print("Original Range:", range_example)
# print("List from Range:", list_from_range)


# # Copying a list using list()
# original_list = [10, 20, 30, 40, 50]
# copied_list = list(original_list)
# print("Original List:", original_list)
# print("Copied List:", copied_list)


# # Using sort() to sort a list
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# numbers.sort() # sort(key=[default=none] , reverse=[default=false])
# print("Sorted List (Ascenging):", numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# numbers.sort(reverse=True) # sort(key=[default=none] , reverse=[default=false])
# print("Sorted List (Descenging):", numbers)


################### Lambda with filter() ##########################################################################
# syntax: filter(function, iterable)


# numbers = [1,2,3,4,5,6,7,8,9,10]
# def is_even(x):
#     return x % 2 == 0
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = list(filter(lambda x: x%2 == 0, numbers))
# print("Original Numbers:", numbers)
# print("Even Numbers:", even_numbers)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = filter(lambda x: x%2 == 0, numbers))
# print(list(even_numbers))


# num = [1,2,3,4,5,6,7,8]
# My_List = list(filter(lambda x: (x%2)!=0, num))
# print(My_List)


################### Lambda with map() ####################################################
# syntax: map(function, iterable, ...)


# numbers = [1,2,3,4,5]
# def double(x):
#     return x * 2
# double_numbers = map(double, numbers)
# print(list(double_numbers))

# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x: x**2, numbers))
# print("Original Numbers:", numbers)
# print("Squared Numbers:", squared_numbers)


# num = [1,2,3,4,5,6,7,8]
# newlist = list(map(lambda a: a**2, num))
# print(newlist)


# num1 = [1,2,3,4,5]
# num2 = [6,7,8,9,10]
# even_numbers = list(map(lambda x,y : x+y, num1, num2))
# print(even_numbers)


################### List Comprehension ##################################

# num = [1,2,3,4,5,6,7,8,9,10]
# squared_even_numbers = [x**2 for x in num if x%2 == 0]
# print(squared_even_numbers)


# students = [
#     ["Alice", 85],
#     ["Bob", 90],
#     ["Charlie", 78],
#     ["David", 92],
#     ["Emma", 88]
# ]

# print(max(students))
# list = max(students, key=lambda a: a[1])
# print(list)

# max_name_student = max(students, key=lambda x: len(x[0]))
# print("Student with maximum length of name:", max_name_student[0])

# first = max(students, key=lambda a: a[1])
# students.remove(first)
# second = max(students, key=lambda a: a[1])
# print(first)
# print(second)


################## Sum ####################################################

# numbers = [1,2,3,4,5]
# sum_of_numbers = sum(numbers)
# print("Original Numbers:", numbers)
# print("Sum of Numbers:", sum_of_numbers)


# numbers = [1,2,3,4,5]
# sum_with_start = sum(numbers, 10)
# print("Original Numbers:", numbers)
# print("Sum with Start Value:", sum_with_start)


#################### Remove ########################################################

# fruits = ["apple", "banana", "orange", "apple", "grape"]
# print("Original List:", fruits)
# fruits.remove("apple")
# print("List after removing 'apple':", fruits)





staffSales=[
["101TGY" , "George" , "Taylor" , 3260 , 5262 , 3745 , 7075 , 1943 , 4400],
["103FCY" , "Fehlix" , "Chayne" , 8717 , 2521 , 5777 , 6189 , 5089 , 6957],
["102SBY" , "Sumren" , "Bergen" , 5012 , 1063 , 7937 , 9560 , 1115 , 5499],
["104SBK" , "Samira" , "Beckle" , 1140 , 9206 , 3898 , 8544 , 5937 , 8705],
["105NBT" , "Nellie" , "Bogart" , 3017 , 3342 , 5939 , 2479 , 3374 , 2297],
["106CGT" , "Cheryl" , "Grouth" , 9620 , 7160 , 5113 , 4803 , 5492 , 2195],
["107DGT" , "Danuta" , "Graunt" , 1583 , 7450 , 1026 , 7463 , 2390 , 6509],
["108JDN" , "Jaiden" , "Deckle" , 4064 , 4978 , 2984 , 3159 , 1464 , 4858],
["109JCK" , "Jimran" , "Caliks" , 6253 , 7962 , 2732 , 7504 , 2771 , 5193],
["110DDN" , "Deynar" , "Derran" , 6305 , 8817 , 5200 , 3647 , 3365 , 1256]
]

for i in staffSales:
    eachtotal = sum(i[3:])
    print(i[1], i[2], eachtotal)
    
teamtotal = sum(sum(i[3:]) for i in staffSales)
print("\nTeam Total", teamtotal)

highlist = sorted(staffSales, key=lambda x: sum(x[3:]), reverse=True)
for i in range(2):
    member = highlist[i]
    print(f"{member[1]} {member[2]} {sum(member[3:])}")
    
    
    