
# file = open('day9_textfile_read.txt', 'r')
#     # Read the entire file content
# content = file.read()
# print(content)
# file.close()


# with open('day9_textfile_read.txt', 'r') as file:
#     # Read one line at a time
#     content = file.readline()
#     print(content)


# with open('day9_textfile_read.txt', 'r') as file:
#     # Read one line at a time
#     content = file.readline()
#     while content:
#         print(content.strip())
#         content = file.readline()
        
        
with open('day9_textfile_read.txt', 'r') as file:
    # Read one line at a time
    content = file.readlines()
    print(content)
 
    for i in content:
        print(i.strip)
 
 
 
 
 
 
    