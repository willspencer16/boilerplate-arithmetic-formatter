def arithmetic_arranger(problems):
    first_row = []
    arithmetic_operator = []
    second_row = []
    dashes = []
    space = ["    "]

    for x in problems:
        list = x.split()

        if len(problems) < 5:
            if len(list[0]) < 5:
                first_row.append(list[0])
            else:
                return "Error: Numbers cannot be more than four digits."

            if list[1] == "+" or list[1] == "-":
                arithmetic_operator.append(list[1])
            else:
                return "Error: Operator must be '+' or '-'."
            
            if len(list[2]) < 5:
                second_row.append(list[2])
            else:
                return "Error: Numbers cannot be more than four digits."

            if len(list[0]) <= len(list[2]):
                dashes.append("-" * (len(list[2]) + 2))
            else:
                dashes.append("-" * (len(list[0]) + 2))
            
    for y in first_row:
        if len(y) == 1:
            space.append("    ")
        elif len(y) == 2:
            space.append("   ")
        elif len(y) == 3:
            space.append("  ")
        elif len(y) == 4:
            space.append("  ")

    for z in second_row:
        if len(z) == 1:
            space.append("    ")
        elif len(z) == 2:
            space.append("  ")
        elif len(z) == 3:
            space.append(" ")
        elif len(z) == 4:
            space.append(" ")

        else:
            return "Error: Too many problems."
    
    arranged_problems = f"{space[1]}{first_row[0]}{space[0]}{space[2]}{first_row[1]}{space[0]}{space[3]}{first_row[2]}{space[0]}{space[4]}{first_row[3]}\n"\
                        f"{arithmetic_operator[0]}{space[5]}{second_row[0]}{space[0]}{arithmetic_operator[1]}{space[6]}{second_row[1]}"\
                        f"{space[0]}{arithmetic_operator[2]}{space[7]}{second_row[2]}{space[0]}{arithmetic_operator[3]}{space[8]}{second_row[3]}\n"\
                        f"{dashes[0]}{space[0]}{dashes[1]}{space[0]}{dashes[2]}{space[0]}{dashes[3]}"
    
    return arranged_problems