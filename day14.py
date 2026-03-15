# Open input file(read mode)
with open("attendance.txt", "r") as infile:
    
    # Open output file(write mode)
    with open("attendance_report.txt", "w") as outfile:
        
        # Write header to output file
        outfile.write("Student Attendance Report\n")
        outfile.write("-------------------------\n")
        
        # Read all lines from input file
        lines = infile.readlines()
        
        # Loop through each line
        for line in lines:
            
            # Remove newlien and split by comma
            data = line.strip().split(",")

            # Extract values
            name = data[0]
            total_classes = int(data[1])
            attended_classes = int(data[2])
            
            # Calculate attendance percentage
            attendance_percent = (attended_classes / total_classes) * 100
            
            # Format result using built-in round() method
            attendance_percent = round(attendance_percent, 2)
            
            # Wrtie result to output file
            outfile.write(f"{name} - {attendance_percent}%\n")
            
print("Attendance report created successfully.")            
        
            
            
            
            