import keyboard

from blackjack_calculator import *
from blackjack_particular_game import *

if __name__ == "__main__":
    while True:
        if re_bet_option_is_available():
            click_re_bet_option()
        if it_is_player_turn():
            dealer_number = read_dealer_number()
            player_number = read_player_number()
            optimal_player_action = "S"
            if split_is_available():
                optimal_player_action = calculate_action_if_split_available(dealer_number, player_number)
            else:
                optimal_player_action = calculate_optimal_player_action(dealer_number, player_number)

            if optimal_player_action == "H":
                go_hit()
            elif optimal_player_action == "D":
                go_double_down()
            elif optimal_player_action == "S":
                go_stand()
            elif optimal_player_action == "P":
                go_split()
            elif optimal_player_action == "R":
                go_surrender()

        if keyboard.is_pressed('esc'):
            break
