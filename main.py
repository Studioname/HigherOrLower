from art import logo
from art import vs
from game_data import data
import random
from replit import clear

score = 0
sorter = []

random.shuffle(data)

def welcome():
  print("Welcome to the Higher or Lower Game! The aim is to guess which option has more followers on Social Media.\n")

def start():
  start = "n"
  while start == "n":
    start = input("Are you ready to begin? Press 'y' to start\n")

def options_to_sorter():
  if not sorter:
    sorter.append(data.pop())
  sorter.append(data.pop())
  sorter.append("placeholder")

def get_string(no):
  print(f"{no}. {sorter[no-1]['name']}, a {sorter[no-1]['description']} from {sorter[no-1]['country']}")

def increment_score(old_score):
  return old_score +1

def guess():
  running = True
  while running == True:

    print(logo)
    global score
    print(f"Your score is {score}.")
    options_to_sorter()
    get_string(1)
    print(vs + "\n")
    get_string(2)

    guess_number = int(input("Which option has more Social Media followers, 1 or 2? Type 1 or 2 to continue."))
  
    if guess_number == 1:
      other_number = 2
    else:
      other_number = 1
    player_guess_followers = sorter[guess_number - 1]['follower_count']
    other_number_followers = sorter[other_number - 1]['follower_count']

    if player_guess_followers > other_number_followers:
      print(f"Well done! {sorter[guess_number - 1]['name']} has {player_guess_followers - other_number_followers} million more followers.")
      score = increment_score(score)
      sorter.pop()
      sorter.pop()
      clear()
    else:
      print(f"Unlucky! {sorter[other_number - 1]['name']} had {other_number_followers - player_guess_followers} million more followers than {sorter[0]['name']}.")
      running = False
    
def game():
  
  welcome()
  start()
  clear()
  guess()

game()