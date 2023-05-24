import math
def rebase(input_base:int, digits:list[int], output_base:int):

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if set(digits) == {0} or digits == [] :
        return [0]
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    

    sum_base_10 = 0
    Number_digits = len(digits)
    for index, digit in enumerate(digits):
        sum_base_10 += digit*input_base**(Number_digits-index-1)
    print(sum_base_10)

    index = 1
    output_digits = list()
    while sum_base_10 > 0:
        digit_output_base = sum_base_10/(output_base**(index-1))
        print(digit_output_base)
        if(digit_output_base>=output_base):
            print("increase index")
            index += 1
        elif(digit_output_base<1):
            print("Decrease index")
            index -= 1
        else:
            new_digit =  math.floor(digit_output_base)
            print("Calculate digit " + str(new_digit))
            print("Calculate position " + str(index))
            output_digits.append((new_digit,index))
            print(new_digit*output_base**(index-1))
            sum_base_10 -= new_digit*output_base**(index-1)
    print(output_digits)
    formatted_output_digits = [0]*output_digits[0][1]

    for element in output_digits:
        formatted_output_digits[output_digits[0][1]-element[1]] = element[0]

    print(formatted_output_digits)
    return formatted_output_digits


print(set([0,0,0,0,0]) == {0})