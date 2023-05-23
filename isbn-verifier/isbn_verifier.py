def is_valid(isbn:str):
    
    scrubbed_isbn = isbn.replace('-', '').lower()
    if len(isbn)!=10:
        return False
    
    control_sum = 0
    digit_position = 10
    for digit in scrubbed_isbn:
        if digit == "x":
            control_sum += 10
        else:
            control_sum += int(digit)*digit_position
        digit_position -= 1
    return control_sum % 11 == 0


if len(isbn)!=: