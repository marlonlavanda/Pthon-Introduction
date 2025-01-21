# If statements = execute some code only if a specified condition is met
# they allow for basic decision making in code
# (if, elif, else)

age = int(input("Enter your age: "))
has_ticket = False
price = 10.00

if age >= 65:
  print("You are a senior.")
  print(f"The ticket price for a senior is ${price * 0.75}")
elif age >= 18:
  print("You are an adult.")
  print(f"The ticket price for an adult is ${price}")
else:
  print("You are a child.")
  print(f"The ticket price for an child is ${price * 0.5}")

if has_ticket:
  print("You can enter the concert.")
else:
  print("You need to buy a ticket.")