# num = int(input("Enter number : "))
# for i in range(1, 13):
#     print(f"{num} x {i} = {num*i}")
    
# for i in range(1, 6):
#     print(i**2)

# sum = 0
# pro = 1
# for i in range(1, 21):
#     sum+=i
#     pro*=i
# print(f"The toatl sum = {sum}")
# print(f"The toatl avarage = {sum/20}")
# print(f"The toatl product = {pro}")

# word = "Python"
# for i in range(len(word)):
#     print(word[i])
    
# for j in word:
#     print(j)


# for i in range(2, 21, 2):
#     print(i)
    
    
# for i in range(1, 31):
#     print(f"{i} x 3 = {i*3}")

# words = ["apple", "banana", "cherry"]
# for i in words:
#     print(i)


# word = "banana"
# count = 0 
# for i in word:
#     if i=="a":
#         count+=1
# print(count)


students = [["SF1", "Ma Ma", 90, 80], 
            ["SF2", "Hla Hla", 20, 40], 
            ["SF3", "Mya Mya", 60, 60]]

roll_no = input("Enter Roll no : ")

# flag = False
# for i in students:
#     if i[0] == roll_no:    
#         tmp = i[2]+i[3]
#         if tmp > 140:
#             result = "Distinction"
#         elif tmp > 130:
#             result = "Merit"
#         elif tmp > 80:
#             result = "Pass"
#         else:
#             result = "Fail"
#         print(i[0], i[1], result)
#         flag = True
#         break
# if flag == False:
#         print("Not Found")
    
for i in students:
    if i[0] == roll_no:    
        tmp = i[2]+i[3]
        if tmp > 140:
            result = "Distinction"
        elif tmp > 130:
            result = "Merit"
        elif tmp > 80:
            result = "Pass"
        else:
            result = "Fail"
        print(i[0], i[1], result)
        break
else:
    print("Not Found")
    