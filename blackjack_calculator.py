# The calculator is based on following image
# https://wizardofodds.com/games/caribbean-blackjack/images/basic-strategy.png

def calculate_action_if_split_available(dealer, player) -> str:
    if player == "4":
        if dealer == "3" or dealer == "4" or dealer == "5" or dealer == "6" or dealer == "7":
            return "P"
        return "H"
    if player == "6":
        if dealer == "4" or dealer == "5" or dealer == "6" or dealer == "7":
            return "P"
        return "H"
    if player == "8":
        if dealer == "5" or dealer == "6":
            return "D"
        return "H"
    if player == "10":
        if dealer == "10" or dealer == "A":
            return "H"
        return "D"
    if player == "12":
        if dealer == "2" or dealer == "3" or dealer == "4" or dealer == "5" or dealer == "6":
            return "P"
        return "H"
    if player == "14":
        if dealer == "8" or dealer == "9" or dealer == "A":
            return "H"
        if dealer == "10":
            return "S"
        return "P"
    if player == "16" or player == "12_soft":
        return "P"
    if player == "18":
        if dealer == "7" or dealer == "10" or dealer == "A":
            return "S"
        return "P"
    if player == "20":
        return "S"


def calculate_optimal_player_action(dealer, player) -> str:
    if player == "5" or player == "6" or player == "7":
        return "H"
    if player == "8":
        if dealer == "5" or dealer == "6":
            return "D"
        return "H"
    if player == "13_soft" or player == "14_soft" or player == "15_soft" or player == "16_soft":
        if dealer == "4" or dealer == "5" or dealer == "6":
            return "D"
        return "H"
    if player == "9" or player == "17_soft":
        if player == "2" or player == "3" or player == "4" or player == "5" or player == "6":
            return "D"
        return "H"
    if player == "10":
        if player == "2" or player == "3" or player == "4" or player == "5" or player == "6" \
                or player == "7" or player == "8" or player == "9":
            return "D"
        return "H"
    if player == "11":
        return "D"
    if player == "12":
        if dealer == "4" or dealer == "5" or dealer == "6":
            return "S"
        return "H"
    if player == "13" or player == "14" or player == "15" or player == "16":
        if player == "2" or player == "3" or player == "4" or player == "5" or player == "6":
            return "S"
        return "H"
    if player == "17" or player == "18" or player == "19" or player == "20" or player == "20_soft":
        return "S"
    if player == "18_soft":
        if dealer == "2" or dealer == "7" or dealer == "8":
            return "S"
        if dealer == "9" or dealer == "10" or dealer == "A":
            return "H"
        return "D"
    if player == "19_soft":
        if dealer == "6":
            return "D"
        return "S"
