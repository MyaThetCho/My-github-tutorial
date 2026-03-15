import re

pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{3}$'

with open("Carplate_Input.txt", "r") as infile, open("Carplate_Output.txt", "w") as outfile:
    for line in infile:
        plate = line.strip()
        
        if re.match(pattern, plate):
            result = f"{plate} - VALID\n"
        else:
            result = f"{plate} - INVALID\n"
            
        outfile.write(result)
        
print("Checking completed. See Output.txt")