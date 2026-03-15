questions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
countries = ["England", "France", "Spain", "Italy", "Germany", "Scotland", "Wales", "United Arab Emirates", "China"]
capitals = ["London", "Paris", "Madrid", "Rome", "Berlin", "Edinburgh", "Cardiff", "Abu Dhabi", "Beijing"]

name = input("Enter Player name : ")
count = 1 
score = 0
done_no = []
while count<=5:
    no = int(input("Enter no between 1 to 9 : "))
    
    while no>len(questions) or (no<=0) or (no in done_no):
        no = int(input("Enter no between 1 to 9 and no can't be repeated : "))  
    
    done_no.append(no)
    no = no-1  
    print(done_no)
    
    print("What is the capital of", countries[no])
    ans = input("Capital : ").lower()
    if ans==capitals[no].lower():
        score+=1
    else:
        print("Incorrect, Capital is :", capitals[no])
        
    count+=1
    
    
print("Player :", name)
print("The score :", score)