# userList = [[110,"Cashin","Bonnie","Cae110",7005],
#             [101,"Cheruit","Madeleine","Che101",1507],
#             [103,"Chanel","Coco","Cho103",7333],
#             [107,"Gres","Madame","Gre107",3054],
#             [114,"Hamnett","Katharine","Hae114",4807],
#             [118,"Herrera","Carolina","Hea118",5567],
#             [111,"Hulanicki","Barbara","Hua111",5125],
#             [116,"Johnson","Betsey","Joy116",8869],
#             [104,"Lanvin","Jeanne","Lae104",8580],
#             [109,"McCardell","Claire","Mce109",5991],
#             [102,"Paquin","Jeanne","Pae102",6495],
#             [112,"Quant","Mary","Quy112",9028],
#             [113,"Rykiel","Sonia","Rya113",1177],
#             [105,"Schiaparelli","Elsa","Sca105",2980],
#             [108,"Schlee","Valentina","Sca108",6801],
#             [106,"Vionnet","Madeleine","Vie106",9042],
#             [117,"Von Furstenberg","Diane","Voe117",2553],
#             [119,"Wang","Vera","Waa119",2004],
#             [115,"Westwood","Vivienne","Wee115",7806]]


# user_acc = input("Enter user acc : ")
# password = int(input("Enter password : "))

# for i in userList:
#     if i[3]==user_acc and i[4]==password:
#         print ("Welcome!", i[1], i[2])
#         Flag = True
#         break
# else:
#     print("Invalid Acc")
    
    
########################################################################    
    
    
# studentTestScores = [
# ["Kevin", "Horney", 71, 55],
# ["Tony", "Tison", 36, 50],
# ["David", "Smith", 39, 48],
# ["Vicky", "Bertwistle", 58, 71],
# ["Jason", "Blashaw", 49, 80],
# ["Louise","Smith", 81, 67],
# ["Sara", "Acton", 37, 66],
# ["Donna", "Alexander", 84, 86],
# ["Michael", "Mitchelle", 65, 55],
# ["Anthony", "Lewis", 48, 50],
# ["Sharon", "Grant", 53, 70],
# ["Peter", "Hughes", 82, 90],
# ["Deborah", "Biddle", 51, 47],
# ["Dawn", "Doens", 35, 44],
# ["William", "Dennis", 72, 73],
# ["Selim", "Biddle", 52, 67],
# ["Ian", "Nadeem", 40, 36],
# ["Jenny", "Thomson", 56, 43],
# ["Rowena", "Moore", 50, 77],
# ["Jane", "Murphy", 44, 48]]
    
# print(f"{"Sr.no":>5} {"Name":^16} {"Total Marks":^15} {"Average":^10} {"Grade":^10}")
# print("-" *55)
    
# no=0
# for i in studentTestScores:
#     no+=1
#     eachtotal = i[2]+i[3]
#     average = round(eachtotal/2)
#     if average >= 70:
#         grade = "Distinction"
#     elif average >= 65:
#         grade = "Merit"
#     elif average >= 40:
#         grade = "Pass"
#     else:
#         grade = "Fail"
#     print(f"{no:>3} . {i[0]+i[1] :<10} {eachtotal:>8} {average:^10} {grade:<10}")
    
    
##########################################################################
    
    
# stblWords = [["apple", "banana"],
#               ["wrist", "leg"],
#               ["blue", "yellow"],
#               ["speaker", "keyboard"],
#               ["lavender", "tulip"],
#               ["pencil", "chalk"],
#               ["apartment", "house"],
#               ["bottom", "top"],
#               ["snow", "fog"],
#               ["beach", "mountain"],
#               ["", ""]]

# word1 = "newspaper"
# word2 = "book"   
    
# stblWords[-1][0]=word1
# stblWords[-1][1]=word2

# for i in stblWords:
#     print(i[0], i[1])
    
#     if len(i[0]) > len(i[1]):
#         print("\t", i[0])
#     else:
#         print("\t", i[1])
        
#     if i[0] > i[1]:
#         print("\t", i[1], i[0])
    
    
#############################################################################


word = input("Enter word : ")
if word == word[::-1]:
    print("Palaindrone")
else:
    print("Not")



