"""Calcualte score from a given set of 5 dice and YATCH category"""

# Score categories.
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
    """ Calcualte the Yath score

    :param dice int[]: a set of 5 6 sided dice
    :param category str: A Yatch category
    :return int: The Score

    Calcualtes the score bassed on the roll (dice) and the category.
    """
    match category:
        case "YACHT":
            # A legal yatch has 5 of a kind equivalent to only having one unique die face
            return 50 if len(set(dice)) == 1 else 0
        case "ONES":
            return dice.count(1)
        case "TWOS":
            return 2 * dice.count(2)
        case "THREES":
            return 3 * dice.count(3)
        case "FOURS":
            return 4 * dice.count(4)
        case "FIVES":
            return 5 * dice.count(5)
        case "SIXES":
            return 6 * dice.count(6)
        case "FULL_HOUSE":
            # Must have two different die faces
            # And any give face must have more than 1 and less than 4 instances
            return sum(dice) if len(set(dice)) == 2 and 1 < dice.count(dice[0]) < 4 else 0
        case "FOUR_OF_A_KIND":
            # Must have two or less unique die faces
            # A given die face must have either 1 or 4 or 5 instances
            # If a given die face has 1 instance, we return 4 times the other unique die face
            # If a given die face has 4 or 5 instances we return 4 times that die face
            if len(set(dice)) > 2:
                return 0
            if dice.count(dice[0]) >= 4:
                return 4 * dice[0]
            if dice.count(dice[0]) == 1:
                return 4 * dice[1]
            return 0
        case "LITTLE_STRAIGHT":
            # Must have 5 unique die faces and cannot contain '6'
            return 30 if len(set(dice)) == 5 and not 6 in dice else 0
        case "BIG_STRAIGHT":
            # Must have 5 unique die faces and cannot contain '1'
            return 30 if len(set(dice)) == 5 and not 1 in dice else 0
        case _:  # CHOICE
            return sum(dice)

    return 0
