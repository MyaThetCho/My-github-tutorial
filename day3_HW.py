libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 26 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]

# total_b = 0
# for b in libraryRecord:
#     total_b+=(b[3])
# print(f"Total number of books : {total_b}") 

# average_b = total_b/(len(libraryRecord))
# print(f"Average number of books : {average_b}\n")
    

# few = []
# for b in libraryRecord:
#     if b[3] < 10:
#         few += [b[0]]
# print(f"ID of pupils who have read fewer than 10 books : {few}")
      
      
# gold_mark = 0 
# for b in libraryRecord:
#     if b[3] > gold_mark:
#         gold_mark = b[3]
#         id = b[0]
#         first_n = b[1]
#         last_n = b[2]
#         t_book = b[3]
# print(f"\nGold Winner : ID {id} - {first_n} {last_n} with total {t_book} books read!")

# silver_mark = 0
# for b in libraryRecord:
#     if b[3] > silver_mark and b[3] < gold_mark:
#         silver_mark = b[3]
#         id = b[0]
#         first_n = b[1]
#         last_n = b[2]
#         t_book = b[3]
# print(f"Silver Winner : ID {id} - {first_n} {last_n} with total {t_book} books read!")

# bronze_mark = 0
# for b in libraryRecord:
#     if b[3] > bronze_mark and b[3] < silver_mark:
#         bronze_mark = b[3]
#         id = b[0]
#         first_n = b[1]
#         last_n = b[2]
#         t_book = b[3]
# print(f"Bronze Winner : ID {id} - {first_n} {last_n} with total {t_book} books read!")







sum = 0
max = libraryRecord[0][3]
min = libraryRecord[0][3]
first = 0
second = 0
third = 0

first_detail = ""
second_detail = ""
third_detail = ""

for i in libraryRecord:
    sum += i[3]
    
    if i[3] < 10:
        print(i[0])
        
    if i[3] > max:
        max=i[3]
        
    if i[3] < min:
        min=i[3]
        
    if i[3] > third and i[3] > second and i[3] > first:
        third = second
        second = first
        first = i[3]
        third_detail = second_detail
        second_detail = first_detail
        first_detail = i
        
    elif i[3] > third and i[3] > second and i[3] < first:
        third = second
        second = i[3]
        third_detail = second_detail
        second_detail = i
        
    elif i[3] > third and i[3] < second and i[3] < first:
        third = i[3]
        third_detail = 1
        
print("The total book :", sum)
print("The Average :", round(sum/len(libraryRecord)))
print("The Max :", max)
print("The Min :", min)
print("\nWinner List")
print("-" * 20)
print(first_detail[0], first_detail[1], first_detail[2], first_detail[3])
print(second_detail[0], second_detail[1], second_detail[2], second_detail[3])
print(third_detail[0], third_detail[1], third_detail[2], third_detail[3])
