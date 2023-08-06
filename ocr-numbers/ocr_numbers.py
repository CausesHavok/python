def parse_digit(input_3by4):
    zero =  [" _ ", "| |", "|_|", "   "]
    one =   ["   ", "  |", "  |", "   "]
    two =   [" _ ", " _|", "|_ ", "   "]
    three = [" _ ", " _|", " _|", "   "]
    four =  ["   ", "|_|", "  |", "   "]
    five =  [" _ ", "|_ ", " _|", "   "]
    six =   [" _ ", "|_ ", "|_|", "   "]
    seven = [" _ ", "  |", "  |", "   "]
    eight = [" _ ", "|_|", "|_|", "   "]
    nine =  [" _ ", "|_|", " _|", "   "]
    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    return str(digits.index(input_3by4))
    
def convert(input_grid):
    digits = []

    rows = len(input_grid)
    columns = len(input_grid[0])

    for i in range(0, rows , 4):
        digits.append([input_grid[i],
                input_grid[i+1],
                input_grid[i+2],
                input_grid[i+3]])
    
    numbers = []
    for digit in digits:
        for i in range(0,columns,3):
            number = parse_digit([digit[0][i:i+3],
                            digit[1][i:i+3],
                            digit[2][i:i+3],
                            digit[3][i:i+3]])
            numbers.append(number)


    return numbers


grid = [
        "    _  _     _  _  _  _  _  _ ",
        "  | _| _||_||_ |_   ||_||_|| |",
        "  ||_  _|  | _||_|  ||_| _||_|",
        "                              ",
        "    _  _     _  _  _  _  _  _ ",
        "  | _| _||_||_ |_   ||_||_|| |",
        "  ||_  _|  | _||_|  ||_| _||_|",
        "                              ",
    ]

print(convert(grid))