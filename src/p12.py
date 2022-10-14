import random
print("Welcome to the game")

pscore = 0
cscore = 0

while True:
  player = input("Rock, Paper, Scissor: ").lower()
  
  game = ["rock","paper","scissor"]
  computer = random.choice(game)
  print("Computer has choosen",computer)
  
  if player == computer:
   print("It's a tie")
  elif player == "rock" and computer == "paper":
    print("Computer wins")
    cscore = cscore + 1
  
  elif player == "paper" and computer == "scissor":
    print("computer wins")
    cscore = cscore + 1
  
  elif player == "paper" and computer == "rock":
    print("player wins")
    pscore = pscore + 1
  
  elif player == "scissor" and computer == "paper":
    print("player wins")
    pscore = pscore + 1
  
  elif player == "rock" and computer == "scissor":
    print("player wins")
    pscore = pscore + 1
  
  elif player == "scissor" and computer == "rock":
    print("computer wins")
    cscore = cscore + 1
  
  
  else:
    print("Wrong choice")
  
  c = input("Do you want to continue(Y/N): ").lower()
  if c == "n":
    print("Thank you")
    print("player score : ",pscore)
    print("Computer score : ",cscore)
    break

