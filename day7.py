number = [5,2,1,7,4,5,5,5]
number.append(10) #add data at back
# number=[] #null array

number.insert(0, 100) #insert data(parameter, data)
number.remove(5) #remove data, only first seen data
# number.clear() #clear the list
number.pop() #delete the last data
number.sort() #sort data accending
number.sort(reverse=True) #sort data decending

print(number.count(5)) #count the given data
print(number)

next=number.copy()
print(next)
