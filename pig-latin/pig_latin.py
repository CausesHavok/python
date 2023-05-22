"""Functions for translating English into pig latin"""
def translate(text:str):
    """Translate text into pig latin
    
    :param text str: Text
    :return str: Text in pig latin
    Translates text into pig latin following rules found on https://exercism.org/tracks/python/exercises/pig-latin
    """
    pig_latin_words = []
    for word in text.split():
        pig_latin_words.append(translate_word(word))

    return ' '.join(pig_latin_words)

def find_vowel(text:str):
    """Finds the fist lower case vowel in a text
    
    :param text str: Indput text
    :return int: index of the first lower case vowel in input text
    """
    vowels_sounds = ("aeiouy")
    index = 0
    for char in text:
        if char in vowels_sounds:
            return index
        index += 1


def translate_word(text:str):
    """Translate a single word into pig latin
    
    :param text str: A word
    :return str: A word in pig latin
    Translates a word into pig latin following rules found on https://exercism.org/tracks/python/exercises/pig-latin
    """
    consonant_sounds = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    vowels_sounds = ("a","e","i","o","u")

    pig_latin = ""
    #Rule 1
    if text.startswith(vowels_sounds) or text.startswith("xr") or text.startswith("yt"):
        pig_latin = text

    #Rule 2-4
    elif text.startswith(consonant_sounds):
        first_vowel = find_vowel(text[1:]) + 1
        if text[first_vowel-1] == "q" and text[first_vowel] == "u": # Rule 3
            pig_latin = text[first_vowel+1:] + text[:first_vowel+1]
        else: #rule 2 and 4
            pig_latin = text[first_vowel:] + text[:first_vowel]

    return pig_latin + "ay"
