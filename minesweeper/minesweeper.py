""" Annotates a minefiled for the classic game Mine Sweeper"""
def annotate(minefield: list[str]):
    """ Annotates a minefiled for the classic game Mine Sweeper
    :param minefield: list[str] - a list of rows represented by strings
    :return: list[str] - an annotated list of rows represented by strings"""
    if not minefield: return []
    row_count = len(minefield)
    column_count = len(minefield[0])
    annotated_minefield = []
    
    for row in range(row_count):
        if column_count != len(minefield[row]):
            raise ValueError("The board is invalid with current input.")
        
        row_text = ""
        for col in range(column_count):
            minefield_elem = minefield[row][col]
            if minefield_elem == "*":
                row_text += "*"
            elif minefield_elem == " ":
                bomb_count = count_adjacent_bombs(minefield, row, col)
                row_text += str(bomb_count) if bomb_count>0 else " "
            else:
                raise ValueError("The board is invalid with current input.")
        annotated_minefield.append(row_text)

    return annotated_minefield


def count_adjacent_bombs(minefield: list[str], i: int, j: int):
    """Counts bombs adjacent to the input field i,j
    :param minefield: list[str] - a list of rows represented by strings
    param i: int - the row number for which the function should compute
    param j: int - the coloumn number for which the function should compute
    return: int - the number of bombs in the up to 9 by 9 grid surrounding i,j
    """
    return sum(minefield[i+ii][j+jj] == "*"
               for ii in [-1, 0, 1]
               for jj in [-1, 0 ,1]
               if 0 <= i + ii < len(minefield)
               if 0 <= j + jj < len(minefield[0]))
