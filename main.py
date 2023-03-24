import random
from players import players
from art import logo

choices=[]
print(logo)

def dice():
  return random.randint(1,len(players))-1


#search choices dictionary for highest age and find position


def game_check(choices):
  guess=""
  total=0
  player1=players[dice()]
  selection2=dice()
  while selection2==player1: #don't let players be the same
    selection2=dice()
  player2=players[selection2]
  choices.append(player1)
  choices.append(player2)
  
  guess=str(input(f"Which choice do you think is older? {choices[0]['name']} or {choices[1]['name']} enter 0 or 1"))
  max_age = 0
  max_age_players = []
  for choice in choices:
    if choice['age'] > max_age:
        max_age = choice['age']
        max_age_players = [choice['name']]
    elif choice['age'] == max_age:
        max_age_players.append(choice['name'])
  
  oldest_player = ", ".join(max_age_players)
  
  if guess == oldest_player:
      print("Win")
      print(f"{choices[0]['name']} is {choices[0]['age']} and {choices[1]['name']} is {choices[1]['age']}")
    
      total+=1
      print(f"Your total is {total}")
      return True
  else:
      print("Lose")
      print(f"{choices[0]['name']} is {choices[0]['age']} and {choices[1]['name']} is {choices[1]['age']}")
      return False

status=True   
while status==True:
  status=game_check(choices)
  

