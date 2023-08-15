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
    for index, digit in enumerate(digits):
        if digit == input_3by4:
            return str(index)
    return "?"


def convert(input_grid):
    digits = []
    columns = len(input_grid[0])
    rows = len(input_grid)

    if rows % 4 != 0: raise ValueError("Number of input lines is not a multiple of four")
    if columns % 3 != 0: raise ValueError("Number of input columns is not a multiple of three")

    numbers = []
    # Parsing 4by3 arrays into digits
    for i in range(0, rows, 4):
        for j in range(0,columns,3):
            number = parse_digit([input_grid[i+0][j:j+3],
                                  input_grid[i+1][j:j+3],
                                  input_grid[i+2][j:j+3],
                                  input_grid[i+3][j:j+3]])
            numbers.append(number)
        numbers.append(",")

    return ''.join(numbers[:-1])
