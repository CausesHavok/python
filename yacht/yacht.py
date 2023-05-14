# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    
    match category:
        case "YACHT":
            return 50 if len(set(dice)) == 1 else 0
        case "ONES":
            return dice.count(1)
        case "TWOS":
            return 2*dice.count(2)
        case "THREES":
            return 3*dice.count(3)
        case "FOURS":
            return 4*dice.count(4)
        case "FIVES":
            return 5*dice.count(5)
        case "SIXES":
            return 6*dice.count(6)
        case "FULL_HOUSE":
            return sum(dice) if len(set(dice))==2 and dice.count(dice[0])>=2 else 0
        case _:
            return 1
    
    return 0
