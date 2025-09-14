def find_bear(input_line):
    # Convert the input line to lowercase for case-insensitive search
    input_line_lower = input_line.lower()
    
    # Check if the full word "bear" is present in the input line
    if " bear " in input_line_lower or input_line_lower.startswith("bear ") or input_line_lower.endswith(" bear"):
        return "There's a bear in there."
    else:
        return "No bears here."
