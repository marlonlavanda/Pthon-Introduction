# logical operators = evaluate multiple conditions (or, and, not)
# or = returns True if at least one condition is True
# and = returns True if all conditions are True
# not = returns True if the condition is False

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
  print("It is hot outside.")
elif temp <= 0 and is_sunny:
  print("It is cold outside.")
elif temp < 28 and temp > 0 and is_sunny:
  print("It is warm outside.")
else:
  print("It is sunny.")