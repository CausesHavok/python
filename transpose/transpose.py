def transpose(lines: str):
    """Transposes a str from rows, columns to columns, rows
    
    :param lines: str - a text.
    :return: str - the transposed text.
    """
    split_lines = lines.split("\n")
    output_lines = []

    for i, string in enumerate(split_lines):
        for j, char in enumerate(string):
            # We add a new string when our exsisting structure can no longer accomodate the ongoing transposing
            if j >= len(output_lines):
                output_lines.append("")
            padding = " "*(i-len(output_lines[j])) # we pad in case one or more previous lines were shorter than the current line
            output_lines[j] += padding + char

    return "\n".join(output_lines)
