import game_data
import art
import random
import game_data
from replit import clear  
game_end = False
def calculate_winner(person_A, person_B):
    followers_person_A = person_A['follower_count']
    followers_person_b = person_B['follower_count']
    if followers_person_A > followers_person_b:
        return "A"
    else:
        return "B"
player_point = 0
def countinue_game():
    clear()
    global player_point
    print(f"You are right! current score {player_point}")
    person_A = random.choice(game_data.data)
    person_B = random.choice(game_data.data)
    winner = calculate_winner(person_A=person_A,person_B=person_B)
    print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}")
    print(art.vs)
    print(f"Compare B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")
    print(winner)
    player_guess = input("Who has more followers? type 'A' or 'b'").upper()
    if player_guess == winner:
        player_point += 1
    else:
        clear()
        print(art.logo)
        print(f"Sorry thats wrong total score: {player_point}")
        return True
print(art.logo)
game_end = False
while game_end != True:
    person_A = random.choice(game_data.data)
    person_B = random.choice(game_data.data)
    winner = calculate_winner(person_A=person_A,person_B=person_B)
    print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}")
    print(art.vs)
    print(f"Compare B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")    
    print(winner)
    player_guess = input("Who has more followers? type 'A' or 'b'").upper()
    if player_guess == winner:
        clear()
        player_point += 1
        while game_end != True:
            game_end = countinue_game()
    else:
        print("You have lost!")

    game_end = True



