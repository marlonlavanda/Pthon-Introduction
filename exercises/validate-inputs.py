# Validate user inputs exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
  print("You're username can't be more than 12 characters.")
elif not username.find(" ") == -1:
  print("Your username can't contain spaces.")
elif not username.isalpha():
  print("Your username can't contain digits.")
else :
  print(f"Welcome {username}!")