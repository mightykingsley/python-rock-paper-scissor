# Function 

# def nobo():
#   print("Hi I'm nobo")
#   print("How can I help you?")

# nobo()

# def fluffy(food):
#   print(f"Hey Henry wanna eat {food}")

# fluffy("fish ball")
# fluffy("sushi")
# a = input("Enter food name: ")
# fluffy(a)

# def display(name,food,hobby):
#   print(f"Hello my name is {name}")
#   print(f"I like to eat {food}")
#   print(f"I like to do {hobby}")

# display("kingsley","curry","games")

def rectangle(l,w):
  area = l*w
  print(f"Area of Rectangle: {area}")

def square(s):
  area = s*s
  print(f"Area of Square: {area}")

def triangle(b,l):
  area = 0.5*b*l
  print(f"Area of triangle: {area}")

print('''Area Calculator
1. Triangle
2. Square
3. Rectangle
4. Exit''')

choice = int(input("Enter your choice: "))
if choice == 1:
  a = int(input("Enter length:"))
  b = int(input("Enter width: "))
  triangle (a,b)

elif choice == 2:
  s = int(input("Enter side: "))
  square (s)

elif choice == 3:
  a = int(input("Enter length: "))
  b = int(input("Enter width: "))
  rectangle (a,b)

elif choice == 4:
  print("Thank you for using the calculator.")

else :
  print("Wrong choice")

Python 10(2)
#string

name = "kingsley"
place = "Hong Kong"

print(f"Hello my name is {name} and I live in {place}")