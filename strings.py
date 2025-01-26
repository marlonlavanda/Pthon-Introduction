name = input("Enter ypur full name: ")
phone_number = input("Enter your phone number: ")
# result = len(name)
# result = name.find("L") # find() returns the index of the first occurence of the specified value
# result = name.rfind("a") # rfind() returns the last index of the first occurence of the specified value
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit() # isdigit() returns True if all characters in the string are digits
# result = name.isalpha() # returns True if all characters are alphabets
# result = phone_number.count("-")
phone_number = phone_number.replace("-", "")

print(phone_number)