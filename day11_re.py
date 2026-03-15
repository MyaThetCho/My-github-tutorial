import re

def validate_car_registration(code):
    pattern = re.compile(r'^[A-Z]{2}\d{2}[A-Z]{3}$')
    return bool(pattern.match(code))
    
valid_codes = ["AB12ABC", "JF45NMB"]
invalid_codes = ["ZMM2KKK", "87JJMN7"]

print("Valid Codes: ")
for code in valid_codes:
    print(f"{code}: {validate_car_registration(code)}")
    
print("\nInvalid Codes: ")
for code in invalid_codes:
    print(f"{code}: {validate_car_registration(code)}")