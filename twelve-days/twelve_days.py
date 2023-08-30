"""Twelve days of Christmas song functionality"""
gifts = ["and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
        ]

days = ["first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"]

def recite(start_verse: int, end_verse: int):
    """ This functions recites the "Twelve Days of Christmas" song from start to end verse

    :param start_verse: int - The starting verse/point for the function
    :param end_verse: int - The ending verse/point for the function
    :return: list[str] - the song starting from the start_verse and ending at the end_verse
    """
    song = []
    for day in range(start_verse-1, end_verse):
        verse = "On the " + days[day] + " day of Christmas my true love gave to me: "
        for i in reversed(range(0, day+1)):
            verse += gifts[i]
        song.append(verse)

    # for the very first verse "On the FIRST day...", we remove the "and" in "and a partridge in a..."
    if start_verse == 1:
        song[0] = song[0].replace("and ", "")

    return song