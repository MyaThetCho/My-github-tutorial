Tbl_city = ["Reggane", "Cairo", "New Delhi", "Muscat", "Athens", "Barcelona", "Havana", "Phoenix", "Brisbane"]
Tbl_temps = ["F103", "F82", "C34", "F95", "C29", "F79", "F84", "C35", "F77"]

while True:
    print("\n--- Temperature Monitoring Syetem ---")
    print("1. Display Table")
    print("2. Update City Temperature")
    print("3. Exit")
    choice = input("Enter your choice : ")
    

    F_total=0
    C_total=0
    if choice == "1":
        print(f"{"\nCity":<15} {"Fahrenheit":>10} {"Celsius":>10}") 
        print("-"*36)
        for i in range(len(Tbl_city)):
            tmp = Tbl_temps[i]
            if tmp[0]=="F":
                F_value = int(tmp[1::])
                C_value = round((F_value-32)+1.8)
            else:
                C_value = int(tmp[1::])
                F_value = round(C_value*1.8+32)
               
            F_total+=F_value
            C_total+=C_value
            print(f"{Tbl_city[i]:<15} {F_value:>5} {C_value:>11}")
        print("-"*36)       
        print(f"{"Overall Average":<15} {F_total//len(Tbl_city):>5} {C_total//len(Tbl_city):>11}")
            
        
    elif choice == "2":
        city = input("Enter name of city : ").lower()
        flag = False
        for j in range(len(Tbl_city)):
            if city == Tbl_city[j].lower():
                flag = True
                print(Tbl_temps[j])
                change_value = input("Enter Change Value : ")
                Tbl_temps[j] = change_value
                print("Updated!", Tbl_city[j], Tbl_temps[j])
        if flag == False:
            print("Invaild City")
        
    else:
        print("Program Ended")
        break




