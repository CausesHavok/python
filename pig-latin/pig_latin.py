import re
"""Functions for translating English into pig latin"""
def translate(text:str):
    """Translate text into pig latin
    
    :param text str: Text
    :return str: Text in pig latin
    Translates text into pig latin following rules found on https://exercism.org/tracks/python/exercises/pig-latin
    """
    pig_latin_sentence = ""
    for word in text.split():
        pig_latin_sentence += translate_word(word) + " "

    return pig_latin_sentence[:-1]


def translate_word(text):
    """Translate a single word into pig latin
    
    :param text str: A word
    :return str: A word in pig latin
    Translates a word into pig latin following rules found on https://exercism.org/tracks/python/exercises/pig-latin
    """

    #Rule 1
    if text[0] in ['a','e','i','o','u'] or text.startswith("xr") or text.startswith("yt"):
        return text+"ay"

    #Rule 3
    matchvar= re.match("[bcdfghjklmnpqrstvwxz]?qu",text)
    if matchvar:
        lengthvar = len(matchvar.group(0))
        return text[lengthvar:] + text[:lengthvar] + "ay"

    #Rule 4
    matchvar= re.match("[bcdfghjklmnpqrstvwxz]+y",text)
    if matchvar:
        lengthvar = len(matchvar.group(0))
        return text[lengthvar-1:] + text[:lengthvar-1] + "ay"
    
    #Rule 2
    matchvar = re.match("y?[bcdfghjklmnpqrstvwxz]*",text) #relies on the fact that there must be a consonant or y
    if matchvar:
        lengthvar = len(matchvar.group(0))
        return text[lengthvar:] + text[:lengthvar] + "ay"

    return "rule5"
