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
    for index, char in enumerate(text):
        if char in "aeiouy":
            return index


def translate_word(text:str):
    """Translate a single word into pig latin
    
    :param text str: A word in english
    :return str: A word in pig latin
    Translates a word into pig latin following rules found on https://exercism.org/tracks/python/exercises/pig-latin
    Functions works by determining the correct place to make a cut in the original word.
    So that "word" becomes "ordway" by cutting "word" between index 0 and index 1
    """
    #Rule 1
    cut_index = 0
    #Rule 2-4
    if not text.startswith(("a","e","i","o","u","xr","yt")):
        cut_index = find_vowel(text[1:]) + 1
     # Rule 3 (no words in english has [consonant]qu other than squ)
    if text.startswith(("qu","squ")):
        cut_index += 1
    
    return text[cut_index:] + text[:cut_index] + "ay"
