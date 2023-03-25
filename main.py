"""Premier League Guessing Game"""

import random
from players import players
from art import logo

choices = [] # this array will only ever contain two players
total = 0 # global variable holds total

def dice():
    return random.randint(1, len(players)) - 1

# search choices dictionary for highest age and find position
def game_check(choices):
    global total # make total a global variable
    guess = ""

    role1 = dice()
    role2 = dice()
    player1 = players[role1]
    while role1 == role2: # don't let players be the same
        role2 = dice()
    player2 = players[role2]
    choices.append(player1)
    choices.append(player2)
    p1 = choices[0]['name']
    p2 = choices[1]['name']
    age1 = choices[0]['age']
    age2 = choices[1]['age']
  
    # Will add a check to see if the ages are the same code above is messy
    while guess != p1 and guess != p2:
        guess = str(input(f"Which choice do you think is older? {p1} or {p2}. Enter full name: "))

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
        print(f"{p1} is {age1} and {p2} is {age2}")
        total += 1 # increment total
        print(f"Your total is {total}")
        choices.clear()
        return True
    elif guess != oldest_player:
        if age1 == age2:
            print("The players are the same age. Let's go again.")
            choices.clear()
            return True
    else:    
        print("Lose")
        print(f"{p1} is {age1} and {p2} is {age2}")
        return False

status = True # user has answered correctly, game goes on
print(logo)
while status == True:
    status = game_check(choices) # starts game
