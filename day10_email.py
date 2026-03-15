file1 = open("day10_email.txt", "r")
file2 = open("day10_emailError.txt", "w")

count=0
for i in file1:
    if "@" not in i:
        count+=1
        file2.write(i)

file2.write("The total number of error is = " + str(count))

file1.close()
file2.close()