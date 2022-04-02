#Rock Paper Scissors Game
import random

play = ["rock" , "paper" , "scissors"]


#Scenarios

again = "yes"


while again == "yes":
   #random computer move
   computer = random.choice(play)
   
   #player input
   player = input("rock, paper, or scissors?: ")
   
   if player == computer: #All Tie Scenarios
      print("Tie!")
   
   elif player == play[0]:
      if computer == play[1]:
         print("You lose! " + computer + " covers " + player)
      else:
         print("You win! " + player + " smashes " + computer)

   elif player == play[1]:
      if computer == play[2]:
         print("You lose! " + computer + " cuts " + player)
      else:
         print("You win! " + player + " covers " + player)
      
   elif player == play[2]:
      if computer == play[0]:
         print("You lose! " + computer + " smashes " + player)
      else:
         print("You win! " + player + " cuts " + computer)
      
      
   else:
      print("I'm sorry. That input is invalid...")
      
   
   again = input("Would you like to play again?(yes/no): ")

print("Thanks for playing!")
   
   