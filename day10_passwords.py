file = open("passwords.txt", "r")


for i in file:
    flag = False
    if i[0].isupper():
        for j in i:
            if j.isdigit():
                flag = True
            
    if flag == False:
        print(i.strip())
        

        
        