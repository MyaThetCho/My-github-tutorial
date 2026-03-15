import random

words = ["antelope", "ape", "badger", "bear", "beaver", "bison", "crocodile", "elephant",
         "elk", "ferret", "goat", "goose", "kangaroo", "llama", "lion", "monkey", "moose",
         "orangutan", "shark", "snake", "tiger", "whale", "wombat"]

random_no = random.randint(0, len(words)-1)
secrect = words[random_no]
print(secrect)
attempt = len(secrect)+3
count = 1

while count<=attempt:
    guess_name = input("Enter you guess : ").lower
    if guess_name == secrect:
        print("Win")
        break
    else:
        print("Wrong")
    attempt+=1