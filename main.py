# Higher Lower game guess who has more Instagram followers
# imports
import random
from art import logo, vs
from game_data import data

# def function to Call data for two random entries in data.
def get_choices():
    """Function to pull account information from data list."""
    for new_coice in data:
        choice = random.choice(data)
        return choice

def compare_choices():
    """Compare Choice 1 vs Choice 2: Return whether Choice 1 > Choice 2"""
    global choice_1, choice_2, c1_follow_greater
    c1_follow = choice_1["follower_count"]
    c2_follow = choice_2["follower_count"]
    c1_follow_greater = True
    # print(f"Choice 1 has {c1_follow} followers, Choice 2 has {c2_follow} followers.") used this line during initial testing
    if c1_follow > c2_follow:
        c1_follow_greater = True
        return c1_follow_greater
    elif c1_follow < c2_follow:
        c1_follow_greater = False
        return c1_follow_greater

# get user choice compare with compare choices
def user_guess():
    global user_score, c1_follow_greater, choice_1, choice_2, is_game_over
    compare_choices()
    user_guess = input(f"If you think choice 1 has more followers type '1' or type '2' if you think choice 2 has more followers.")
    if user_guess == "1":
        user_g = True
    elif user_guess == "2":
        user_g = False
    if user_g == c1_follow_greater:
        user_score += 1
        choice_1 = choice_2
        choice_2 = get_choices()
        print("\033c", end="")
        print(logo)
        print(f"Correct answer, your score is now {user_score}")        
    elif user_g != c1_follow_greater:
        is_game_over = True
        print("\033c", end="")
        print(logo)
        print(f"Incorrect, you got {user_score} correct. Good Try.")        
    else:
        print("Invalid input.")

def format_data(account):
    """Format account data"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

# Game Play
def play_game():
    """Game Play"""
    global choice_1, choice_2
    print(f"Compare 1: {format_data(choice_1)}")
    print(vs)
    print(f"Compare 2: {format_data(choice_2)}")
    # print(compare_choices()) used during testing
    user_guess()
# def function to compare a vs b. return highest follower count.

# Global Variables
user_score = 0
is_game_over = False
choice_1 = get_choices()
choice_2 = get_choices()
if choice_1 == choice_2:
    choice_2 = get_choices()
c1_follow_greater = False

while not is_game_over:
    play_game()