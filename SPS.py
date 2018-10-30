"""Stone-Paper-Scissors"""

from random import randint
import time
options=["STONE","PAPER","SCISSORS"]
message={}
message={"tie":"Yawn it's a tie!",
        "won":"Yay you won!",
        "lost":"Aww you lost!"}

def decide_winner(user_choice,computer_choice):
  print str("Your Choice: "+user_choice)
  time.sleep(1)
  print str("Computer's Choice: "+computer_choice)
  time.sleep(2)
  if user_choice==computer_choice:
    print message["tie"]
  elif user_choice==options[0] and computer_choice==options[2]:
    print message["won"]
  elif user_choice==options[1] and computer_choice==options[0]:
    print message["won"]
  elif user_choice==options[2] and computer_choice==options[1]:
    print message["won"]
  else:
    print message["lost"]
    
def play_SPS():
  user_choice=raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice=user_choice.upper()
  computer_choice=options[randint(0,2)]
  decide_winner(user_choice,computer_choice)
  
play_SPS()
