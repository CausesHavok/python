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
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


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
        case "FOUR_OF_A_KIND":
            unique_dice = set(dice)
            if len(unique_dice)!=2:
                return 0
            if dice(dice.count(dice[0])) == 4:
                return 4 * dice[0]
            if dice(dice.count(dice[0])) == 1:
                return 4 * dice[1]
            return 0
        case "LITTLE_STRAIGHT":
            return len(set(dice))==5 and not 6 in dice
        case "BIG_STRAIGHT":
            return len(set(dice))==5 and not 1 in dice
        case _: # CHOICE
            return sum(dice)
    
    return 0
