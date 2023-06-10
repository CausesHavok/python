def answer(question:str):
    #replace words with operators
    question = question.replace("multiplied by","*").replace("divided by","/").replace("plus", "+").replace("minus", "-")
    #Grab essential part of question
    parts = question.rstrip("?").split()[2:]

    if not parts:
        raise ValueError("syntax error")
    
    print(parts)
    operator = "+"
    value = 0
    for index, part in enumerate(parts):
        if index % 2:
            if part in [ "+", "-", "*", "/"]:
                operator = part
            else:
                raise ValueError("syntax error")
        else:
            parse_number(part)
            if operator == "+":
                value = value + int(part)
            elif operator == "-":
                value = value - int(part)
            elif operator == "/":
                value = value / int(part)
            elif operator == "*":
                value = value * int(part)
            else:
                raise ValueError("unknown operation")
            operator = ""

    if operator != "":
        raise ValueError("syntax error")
    return value


def parse_number(part: str):
    if not(part.isdigit() or part[0] == "-" and part[1:].isdigit):
        raise ValueError("syntax error")



print(answer("What is 1 plus?"))