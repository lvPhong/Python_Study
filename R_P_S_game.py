
import getpass

RPS_GAME_CHOICES = ('r', 'p', 's')

def again_still_right_choice(player_name):
    player_choice = getpass.getpass("\nEnter your "+ str(player_name) + " choice:  ")
    # print(type(player_choice))
    while str(player_choice).lower() not in RPS_GAME_CHOICES:
        print("-"*30)
        print("""
            Please enter your choice again
            Your answer must be in {'r', 's', 'p'} to run the game.
            """)
        print("-"*30)
        player_choice = getpass.getpass("\nEnter your choice again")
    return player_choice

def get_players_choice():
    print("-"*30)
    first_player_choice = again_still_right_choice("first player")
    
    print("-"*30)
    second_player_choice = again_still_right_choice("second player")

    player_choices = (first_player_choice, second_player_choice)

    return player_choices


def check_result_rps_game(player_choices):
    first_player_win = "first player win"
    second_player_win = "second player win"
    two_player_draw = "two player draw"

    first_player_win_cases = [('r', 's'), ('s', 'p'), ('p', 'r')]
    second_player_win_cases = [('s', 'r'), ('p', 's'), ('r', 'p')]
    two_player_draw_cases = [('r', 'r'), ('s', 's'), ('p', 'p')]

    if player_choices in first_player_win_cases:
        return first_player_win
    if player_choices in second_player_win_cases:
        return second_player_win
    if player_choices in two_player_draw_cases:
        return two_player_draw

def display_rps_rule():
    print("-"*50)
    print("ROCK - PAPER - SCISSORS GAME\n")
    print("-"*50)
    print("""
        RULE OF ROCK- PAPER - SCISSORS GAME:
        ROCK beats SCISSORS
        SCISSORS beats PAPER
        PAPER beats ROCK
        """)
    print("-"*50)
    print("""
        Enter your choice:
            'r' for ROCK
            'p' for PAPER
            's' for SCISSORS
        """)

def is_play_again():
    while True:
        print("-"*50)
        again_request = input("Do you want to play again? 'y' or 'n' for YES or NO:  ")
        player_answer = again_request.lower()
        if player_answer in ['y', 'n']:
            break
    if player_answer == 'y':
        return True
    else:
        return False

def rps_game():
    while True:
        display_rps_rule()

        player_choices_ = get_players_choice()
        rps_result = check_result_rps_game(player_choices_)

        print(rps_result)
        print("\nFirst player choose: ", player_choices_[0])
        print("\nSecond player choose: ", player_choices_[1])
        
        if is_play_again() == True:
            continue
        else:
            break

# start rps-game
rps_game()
