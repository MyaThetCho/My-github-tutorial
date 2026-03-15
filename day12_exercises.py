# import re

# def contains_python(input_string):
#     # pattern = re.compile(r'python', re.IGNORECASE)
#     pattern = re.compile(r'\bpython\b', re.IGNORECASE) 
#     return bool(pattern.search(input_string))

# # Test cases
# test_string_1 = "I love Python programming!"
# test_string_2 = "Java is my favorite language."
# test_string_3 = "Pythoneasyone"

# print(contains_python(test_string_1)) # Output: True
# print(contains_python(test_string_2)) # Output: False
# print(contains_python(test_string_3))

#================

# text = "I love Python programming. Pythonaaa is great! Python"
# print(re.findall(r'\bPython', text))
# print(re.findall(r'\bPython\b', text))





#################################################################################################


# import re

# def validate_email(email):
#     pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
#     return bool(pattern.match(email))

# # Test Cases
# # Test cases
# valid_email_1 = "user123@example.com"
# valid_email_2 = "john_doe.42@example.co.uk"
# invalid_email_1 = "invalid.email@"
# invalid_email_2 = "missing_at_sign.com"

# print(validate_email(valid_email_1)) # Output: True
# print(validate_email(valid_email_2)) # Output: True
# print(validate_email(invalid_email_1)) # Output: False
# print(validate_email(invalid_email_2)) # Output: False



########################################################################################################


# import re

# def extract_phone_numbers(text):
#     pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
#     return pattern.findall(text)

# # Test Case
# sample_text = """
# John's phone number is 123-456-7890.
# Alice can be reached at 987-654-3210 or 555-123-4567.
# Invalid numbers: 12-345-6789, 1234-567-8901.
# """

# phone_numbers = extract_phone_numbers(sample_text)
# print(phone_numbers)


# ==========================


# import re

# def extract_mm_phone_numbers(text):
#     pattern = re.compile(r'\+95-\d{7,9}\b')
#     return pattern.findall(text)


# # Test case
# sample_text = """
# John's Myanmar number is +95-945678901.
# Alice can be reached at +95-987654321 or +95-912345678.
# Invalid numbers: +95-12345, 095-987654321.
# """

# phone_numbers = extract_mm_phone_numbers(sample_text)
# print(phone_numbers)


# ===========================

# import re

# pattern = re.compile(r'\+95-\d{7,9}')
# # pattern = re.compile(r'\+95-\d{7,9}\b')
# text = "Call me at +95-9876543210abc"
# print(pattern.findall(text))


###################################################################################################


# import re

# def validate_password(password):
#     # Password must be at least 8 characters long
#     # and include at least one uppercase letter, one lowercas letter, and one digit
#     pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
#     return bool(pattern.match(password))


# # Test cases
# valid_password_1 = "Passw0rd"
# valid_password_2 = "Secure123"
# invalid_password_1 = "weakpass"
# invalid_password_2 = "NoNumOrUpperCase"


# print(validate_password(valid_password_1)) # Output: True
# print(validate_password(valid_password_2)) # Output: True
# print(validate_password(invalid_password_1)) # Output: False
# print(validate_password(invalid_password_2)) # Output: False


# ============================

# import re

# def validate_password(password):
#     # Password must be at least 8 characters long
#     # and include at least one uppercase letter, one lowercas letter,
#     # one digit, and one special character(!@#$%^&*)
#     pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$')
#     return bool(pattern.match(password))

# # Test cases
# valid_password_1 = "Passw0rd!"     # OK → lowercase, uppercase, digit, special
# valid_password_2 = "Secure#123"    # OK
# invalid_password_1 = "weakpass1"   # no uppercase, no special
# invalid_password_2 = "StrongPass"  # no digit, no special
# invalid_password_3 = "Pass1234"    # no special


# print(validate_password(valid_password_1)) # Output: True
# print(validate_password(valid_password_2)) # Output: True
# print(validate_password(invalid_password_1)) # Output: False
# print(validate_password(invalid_password_2)) # Output: False
# print(validate_password(invalid_password_3)) # Output: False



##################################################################################################3


# import re

# # Test Case
# tweet = "Excited to share my latest project! #Python #FSUni #Coding"

# # Define the regular expression pattern for hashtags
# pattern = re.compile(r'#\w+') # one or more word characters (\w+)

# # Use finall to extract all hashtags from the tweet
# hashtags = pattern.findall(tweet)

# # Print the extracted hashtags 
# print("Extracted Hashtags:", hashtags)



###################################################################################################3


# word_list = ["Apple", "Banana", "Orange", "grape", "apricot"]

# # startwith method is used after converting each string to lowercase
# # to ensure a case-insensitive comparison
# filtered_strings = [s for s in word_list if s.lower().startswith('a')]

# print("Filterde Words:", filtered_strings)


######################################################################################################


# import re

# text = "Some dates in the text: 1/15/2022, 02/28/2023, 12/31/2021, 1/1/2023"

# # Define the regular expression pattern for dates in "MM/DD/YYYY" format
# date_pattern = re.compile(r'\b(\d{1,2}/\d{1,2}/\d{4})\b')

# # Use fineall to extract all dates from the text
# dates = date_pattern.findall(text)

# # Print the extracted dates
# print("Extracted Dates:", dates)



###################################################################################################


# original_text = "I have an apple. Apples are delicious!"

# updated_text = original_text.lower().replace("apple", "orange", -1)

# print("Original Text:", original_text)
# print("Updated Text:", updated_text)


# '''
# replace(old, new, count)
# without count --> all (default)
# count = 1 --> first one
# count = 2 --> first two
# count = -1(or negative number) --> all (same with default)
# '''


######################################################################################################


import re

# Example usage
time = "14:30"

# Define regex pattern for HH:MM format
time_pattern = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')
match = time_pattern.match(time)

# Print the validation result
print(f'Time "{time}" is valid: {bool(match)}')

'''
^                 string start
([01]\d|2[0-3])   hours (00-19 or 20-23)
:                 colon separator
([0-5]\d)         minutes (00-59)
                  ([0-5]\d) ဆိုတာ
                  first digit = 0-5
                  second digit = 0-9
                   
$                 string end


'''



