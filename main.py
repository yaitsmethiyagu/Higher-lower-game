from art import logo, vs, win, lose
import random
from game_data import data
from replit import clear

is_on = True

def pick_random_data():
  selected_data = random.choice(data)
  #print(selected_data)
  return selected_data

def which_is_higher(option1, option2):
  a_followers = option1["follower_count"]
  b_followers = option2["follower_count"]
  
  if a_followers > b_followers:
    return option1
  else:
    return option2
  

def print_data(data, option):
  name = data['name']
  desctiption = data['description']
  country = data['country']
  print(f"{option}: {name} from {country}, {desctiption}")
  
def validate_choice(choice, a, b):
  while choice != "a" and choice != 'b':
    print('invalid entry, retry')
    choice = input("\nwho has higher Followers in Instagram? \nA or B ?:  ").lower()

  a_followers = a["follower_count"]
  b_followers = b["follower_count"]
  maximum = max(a_followers, b_followers)
  
  option_list = [a_followers, b_followers]
  if option_list[0] > option_list[1]:
    higher_option = "a"
  else:
    higher_option = "b"

  if a_followers == b_followers:
    print(f"oh no, it is a tie. Both same same followers {a_followers}M")

  
  elif choice == higher_option:
    print(f"\n{win} you are right. \nA followers is {a_followers}M \nB followers is {b_followers}M \n{maximum}M is higher")
    return "win"
    
  else:
    print(f"\n{lose} you are Wrong. \nA followers is {a_followers}M \nB followers is {b_followers}M \n{maximum}M is higher")
    return "lose"




  
while is_on:
  user_score = 0
  clear()
  print(logo)
  print("WELCOME TO HIGHER - LOWER GAME \n")
  option_1_data = pick_random_data()
  

  winning = True

  while winning :
    
    print_data(option_1_data, "Option A")  
    print(vs)
    
    option_2_data = pick_random_data()
    if option_1_data == option_2_data:
      option_2_data = pick_random_data()
    print_data(option_2_data, "Option B")
  
    user_choice = input("\nwho has higher Followers in Instagram? \nA or B ?:  ").lower()
    result = validate_choice(user_choice, option_1_data, option_2_data)

  
    if result == "win":
      user_score += 1
      print(f"\nYour Score is {user_score} \nNext Quizz...\n")
      option_1_data = which_is_higher(option_1_data, option_2_data)
    
    else:
      print(f"\nYour Score is {user_score}.\n")
      winning = False
  replay = input("\nReplay? type 'y' for yes: ")
  if replay == "y":
    is_on = True
  else:
    is_on = False
    
    

  
  #is_on = False