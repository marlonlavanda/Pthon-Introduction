# List [] = mutable, most flexible, can be used as a stack, queue, or deque
# Tuple () = immutable, faster than lists, can be used as dictionary keys
# Set {} =  mutable (add/remove),unordered, unique elements, can be used for membership testing

#fruits = ["apple", "banana", "cherry", "orange", "elderberry", "fig", "grape"]
#fruits = ("apple", "banana", "cherry", "orange", "grape")
fruits = {"apple", "banana", "cherry", "orange", "grape"}

#fruits.append("mango")
#fruits.remove("banana")
#fruits.pop(3)
#fruits.clear()

#fruits.add("mango")

for fruit in fruits:
  print(fruit, end=" ")

fruit_search = input("\nEnter a fruit to search for: ")

# Example of membership testing
if fruit_search in fruits:
  print(f"{fruit_search} is in the fruits set")
else:
  print(f"{fruit_search} was not found")
