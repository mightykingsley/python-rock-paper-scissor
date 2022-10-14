# for a in range(1,78):
#   print(a,"Person")
#   if a == 31:
#     print("0 person")
#     break

# import random
# for a in range(15):
#   dice = random.randint(1,63)
#   print(dice)

import random
num = random.randint(1,20)

while True:
  guess=int(input("Guess a numer: "))
  
  if num == guess:
    print("You are correct")
    break
  
  elif guess > num:
    print("Too high")
  
  elif guess < num:
    print('Too low')