from operator import truediv


print("Hello World")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "John"
character_age = "35"

print("My name is " + character_name + " and my age is " + character_age + "")


def say_hi (name): 
  print("hello " + name)

say_hi("Mike")

# a function to cube a number 
# using a return
def cube(num):
  return num * num * num
result = cube(3)
print(result)

# if statements
is_male = False
is_tall = False
# comment comment comment
if is_male:
  print("Yes, male")
else:
  print("No, Female")

if is_male or is_tall:
  print("Tall Male")
elif is_male and not(is_tall):
  print("Short Male")
elif not(is_male) and is_tall:
  print("Tall Female")
else:
  print("Not Male Not Tall")   
