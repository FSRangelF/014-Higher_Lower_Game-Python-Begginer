import os
import time
import random
import art
import game_data

def clear_console():
    """Clears the console screen based on the operating system."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def extract_data():
  global data
  ind = random.randint(0,len(data)-1)
  option = data[ind]
  data.pop(ind) 
  return option

def compare(A, B, choice):
  if A['follower_count'] >= B['follower_count']:
    return choice == "A"
  else:
    return choice == "B"

data = game_data.data 
game_over = False

score = 0

option_A = extract_data()

while not game_over:
  clear_console()
  print(art.logo)

  option_B = extract_data()

  print(f"\nCompare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
  print("\n")
  print(art.vs)
  print(f"\nAgainst B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  while guess != "A" and guess != "B":
    guess = input("Invalid option. Please type 'A' or 'B': ").upper()
  
  result = compare(A=option_A, B=option_B, choice=guess)

  option_A = option_B

  if result:
    score += 1
  else:
    clear_console()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    game_over = True

  if len(data) == 0:
    clear_console()
    print(art.logo)
    print(f"You guessed all comparisions right and attained max score. Final score: {score}")
    game_over = True
