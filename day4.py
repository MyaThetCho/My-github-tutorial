# pupilAttendance = [["Faroukh" , "Salah" , 70],
# ["Kelvin", "Glintode" , 85],
# ["Lara" , "Godfrey" , 90],
# ["Amara" , "Grzinski" , 70],
# ["Aaron" , "Grimshaw" , 90],    
# ["Farihaa" , "Mohan" , 95],
# ["Taz" , "Grimstow" , 60],
# ["Ali" , "Aisha" , 95],
# ["Charlene" , "Hall" ,85],
# ["Asra" , "Ashiq" , 90],
# ["Sadia" , "Bhatti" , 65],
# ["Ria" , "Hall" , 90],
# ["Fernado" , "Askabat" , 60],
# ["Richard" , "Hawkins" , 80],
# ["Siyao" , "Wang" , 60],
# ["Marketta" , "Hosier" , 100]]

# count = 0
# number = 1
# print("The students list of under 75%")
# print('=' * 25)
# for i in pupilAttendance:
#     if i[2] < 75:
#         print (str(number) + "." , i[0], i[1])
#         number+=1
        
#     if i[2] >= 90:
#         count += 1
# print("\nThe total count :", count)













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

total = 0
first = 0
second = 0
f_name = ""
s_name = ""
print("Total sales of each member")
print('-' * 25)
for i in staffSales:
    each_total = i[3] + i[4] + i[5] + i[6] + i[7] + i[8]
    print(i[1], i[2], "\t", each_total)
    total+=each_total
    
    if each_total > second and each_total > first:
        second = first
        first = each_total
        s_name = f_name
        f_name = i
    elif each_total > second and each_total < first:
        second = each_total
        s_name = i
    
print("\nTotal sales by the whole team :", total)
print(f_name[1], f_name[2], first)
print(s_name[1], s_name[2], second)