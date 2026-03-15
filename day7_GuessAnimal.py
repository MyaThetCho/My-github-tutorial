import random

# Array of words
words = ["antelope", "ape", "badger", "bear", "beaver", "bison", "crocodile", "elephant",
         "elk", "ferret", "goat", "goose", "kangaroo", "llama", "lion", "monkey", "moose",
         "orangutan", "shark", "snake", "tiger", "whale", "wombat"]

random_no=random.randint(0, len(words)-1)
print(words[random_no])
secrete = words[random_no]
attempt = len(secrete)+3
print(attempt)
count = 1
print("Hint :", len(secrete))
correct = []
incorrect = []

while (count<=attempt):
    guess_name = input("Enter you guess animal : ").lower()
    
    while len(secrete)!=len(guess_name):
        guess_name = input("Enter again guess animal : ").lower()
    
    if secrete == guess_name:
        print("Win!!! At attempt :", count)      
        break
    else:
        print("Wrong")
        
        for i in guess_name:
            if i in secrete:
                if i not in correct:
                    correct.append(i)
            else:
                if i not in incorrect:
                    incorrect.append(i)
                
        print(correct)
        print(incorrect)
       
       
    count+=1
    