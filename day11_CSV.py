import csv

data = [
    ['Name', 'Age', 'Country'],
    ['Alice', 25, 'USA'],
    ['Bob', 30, 'Canada'],
    ['Charlie', 22, 'UK']
]

# with open ('Output.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)
    
    
with open ('Output.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
        
