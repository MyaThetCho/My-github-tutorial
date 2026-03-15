# with open('day10_fileWrite.txt', 'w') as file:
#     file.write('Hello, World\n')
#     file.write('This is a file writing example.\n')

# with open('day10_fileWrite.txt', 'a') as file:
#     file.write('Append sentence1.\n')
#     file.write('Append sentence2.\n')
    
   
# lines = [
#     'Line 1: Hello,World!\n',
#     'Line 2: Welcome to python programming.\n',
#     'Line 3: This is a file reading example.\n'
# ]
# with open('day10_fileWrite.txt', 'w') as file:
#     # Write the list of strings to the file
#     file.writelines(lines)


# fruit = ["Apple", "Orange", "Banana", "Papaya"]
# file = open('day10_fileWrite.txt', 'w')
# for i in fruit:
#     file.write(i + ",")
# file.close()

# fruitlist = []
# file = open('day10_fileWrite.txt', 'r')
# fruitlist = file.read().split(",")
# print(fruitlist)
# file.close()



# gameScores = [['Alexis', 1, 19], ['Seema', 1, 29], ['Seema', 2, 44], ['Lois', 1,10], 
# ['Alexis', 2, 17], ['Alexis', 3, 36], ['Dion', 1, 23], ['Emma', 1, 27],
#  ['Emma', 2, 48]]

# file = open('day10_fileWrite.txt', 'w')
# for i in gameScores:
#     file.write(str(i) + ",")
    
# file.close()


# Creating a text file with some lines of text
with open('day10_fileWrite.txt', 'r') as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Number of words in the file: {word_count}")



###################################################################################

############### text spliting ###############

# text = "Python is an amazing language"
# words = text.split()
# print(words)


# csv_text = "apple,banana,grape,orange"
# fruits = csv_text.split(',')
# print(fruits)


# date = "2024-08-18"
# parts = date.split('-')
# print(parts)


# text = "a quick brown fox jumps over the lazy dog"
# result = text.split(' ', 3)
# print(result)


