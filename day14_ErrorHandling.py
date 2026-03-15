######################### Try - Except - Finally #################################################

# try:
#     age = int(input("Age : "))
#     print(age)
# except ValueError:
#     print("Invalid Value")
    
   
   


def divide_numbers(x,y):
    try:
        result = x/y
        print(f"The reult of {x}/{y} is : {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An uneecepted error occurred: {e}")
    finally:
        print("This block always executes, whether an exception occurs or not.")

# Example usage:
# Uncomment one of the scenarios to see erroe handling in action.

# Scenrio 1: Divide by Zero
divide_numbers(10, 0)

# Scenario 2: Invalid data type
divide_numbers(10, "2")

    