def arithmetic_arranger(problems, display=False):
    first_row = []
    second_row = []
    dashes = []
    answers = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in range(len(problems)):
        list = problems[problem].split()

        if not list[0].isdigit():
            return "Error: Numbers must only contain digits."
        elif not list[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(list[0]) < 5:
            if len(list[0]) >= len(list[2]):
                first_row.append("  ")
                first_row.append(list[0])
                first_row.append("    ")
            else:
                first_row.append(" " * ((len(list[2]) - len(list[0]) + 2 )))
                first_row.append(list[0])
                first_row.append("    ")
        else:
            return "Error: Numbers cannot be more than four digits."

        if list[1] == "+" or list[1] == "-":
            second_row.append(list[1])
        else:
            return "Error: Operator must be '+' or '-'."
        
        if len(list[2]) < 5:
            if len(list[0]) <= len(list[2]):
                second_row.append(" ")
                second_row.append(list[2])
                second_row.append("    ")
            else:
                second_row.append(" " * ((len(list[0]) - len(list[2]) + 1 )))
                second_row.append(list[2])
                second_row.append("    ")
        else:
            return "Error: Numbers cannot be more than four digits."

        if len(list[0]) <= len(list[2]):
            dashes.append("-" * (len(list[2]) + 2))
            dashes.append("    ")
        else:
            dashes.append("-" * (len(list[0]) + 2))
            dashes.append("    ")
        
        if len(list[0]) <= len(list[2]):
            answers.append(" " * ((len(list[2]) + 2) - len(str(eval(problems[problem])))))
            answers.append(str(eval(problems[problem])))
            answers.append("    ")
        else:
            answers.append(" " * ((len(list[0]) + 2) - len(str(eval(problems[problem])))))
            answers.append(str(eval(problems[problem])))
            answers.append("    ")
    
    first_row = first_row[:-1]
    second_row = second_row[:-1]
    dashes = dashes[:-1]
    answers = answers[:-1]

    if display == True:
        arranged_problems = ''.join(first_row) + "\n" + ''.join(second_row) + "\n" + ''.join(dashes) + "\n" + ''.join(answers)
    else:
        arranged_problems = ''.join(first_row) + "\n" + ''.join(second_row) + "\n" + ''.join(dashes)
            

    return arranged_problems