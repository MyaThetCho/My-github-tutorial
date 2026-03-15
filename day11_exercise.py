# file = open("sales.txt", "r")
# total = 0

# for i in file:
#     tmp=i.strip() #remove white space/line
#     tmp=tmp.split(',') #parsing token
#     # print(tmp)
    
#     sub = 0
#     for j in tmp:
#         sub+=int(j)
#     print(sub)
#     total+=sub
    
# print("Grand Total", total)

# file.close()
    
 
###########################################################################################33


# gameScores = [['Alexis', 1, 19], ['Seema', 1, 29], ['Seem', 2, 44], ['Lois', 1, 10],
#               ['Alexis', 2, 17], ['Alexis', 3, 36], ['Dion', 1, 23], ['Emma', 1, 27],
#               ['Emma', 2, 48]]   

# file = open("TestFile.txt", "w")
# for i in gameScores:
#     file.write(str(i)+ ",")
    
# file.close()
    

#############################################################################3#######################


tbl_tuna = [["Yellowfin",105,15,3],
            ["Albacore",90,15,5],
            ["Skipjack",50,3,4],
            ["Bigeye",105,25,4],
            ["Atlantic Bonito",50,4,2],
            ["Northern Bluefin",190,120,11],
            ["Southern Bluefin",190,120,11],
            ["Tongol",90,20,4]]


# file = open("TunaData.txt", "w")
# no = 101
# for i in tbl_tuna:
#     tmp = str(no) + "," + i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "\n"
#     file.write(tmp)
#     no += 1
# file.close
    


code_number = 101

for row in tbl_tuna:
    row.insert(0, code_number)
    # insert(index, value)
    code_number += 1
    
# print(tbl_tuna)

import csv
with open('TunaData.csv', 'w', newline='') as file:
    # newline='', FORMAT FOR CSV ဖိုင်ထဲကိုလိုင်းအသစ်ထပ်မထည့်ပါနဲ့
    writer = csv.writer(file)
    writer.writerows(tbl_tuna)

