# shop = ["Iphone","Play Stations","speakers"]
# item = input("What do you want? to buy?")
# if item in shop:
#   print("It's right there")
# else:
#   print("This item is out of sell")

# append()

# games =[]
# for a in range(4):
#  b = input("Enter games: ")
#  games.append(b)
# print(games)
shop = ["sugar","carrot","fishball","ice cream",""]
cart = []
while True:
 
 item = input("What do you want?").lower()
 if item in shop:
  print("it's right here")
  cart.append(item)
 
 elif item == "checkout":
  print("Thank you for shopping")
  print("You bought",cart)
  break
 else:
  print("sorry is we don't have that")

Python 9(2)
import random
food = ["pizza","hambergur","chicken nuggets","curry","ice cream","lobster","crab"]
ingredients =["suger","salt","oil","ketchup","honey"]
for c in range(1,6):
   a = random.choice(ingredients)
   b = random.choice(food)

   print("Add",a,"to",b)