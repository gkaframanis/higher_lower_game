import random
from subprocess import call 
import os
import art
from game_data import data


def clear(): 
    _ = call('clear' if os.name =='posix' else 'cls') 


def choose_personality(data):
    person = random.choice(data)
    return person

def check_guess(followers_1, followers_2, guess):
    if followers_1 > followers_2 and guess == "A":
        return True
    if followers_1 > followers_2 and guess == "B":
        return False
    if followers_1 < followers_2 and guess == "B":
        return True
    if followers_1 < followers_2 and guess == "A":
        return False

def format_data(personality):
    personality_name = personality["name"]
    personality_desc = personality["description"]
    personality_country = personality["country"] 
    return f"{personality_name}, a {personality_desc}, from {personality_country}"   


score = 0
has_ended = False
answer = False
while not has_ended:
    clear()
    print(f"{art.logo}\n")
    
    if answer == True:
        print(f"You're right! Current score: {score}")
    
    personality_1 = choose_personality(data)
    personality_2 = choose_personality(data)

    if personality_1 == personality_2:
        personality_2 = choose_personality(data)


    print(f"Compare A: {format_data(personality_1)}\n")

    print(f"{art.vs}\n")

    print(f"Against B: {format_data(personality_2)}\n")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    if check_guess(personality_1["follower_count"], personality_2["follower_count"], guess):
        score += 1
        answer = True
    else:
        answer = False
        has_ended = True

clear()
print(f"{art.logo}\n")
print(f"Sorry, that's wrong. Final score: {score}")



