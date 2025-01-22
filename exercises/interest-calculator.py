# Program to compound interest calculator

principle = 0
rate = 0
time = 0

while True:
  principle = float(input("Enter the principle amount: "))
  if principle < 0:
    print("Principle amount cannot be less than zero.")
  else:
    break

while True:
  rate = float(input("Enter the rate amount: "))
  if rate < 0:
    print("Interest rate cannot be less than zero.")
  else:
    break

while True:
  time = int(input("Enter the time in years: "))
  if time < 0:
    print("Time cannot be less than or equal to zero.")
  else:
    break


total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years/s: ${total:.2f}")