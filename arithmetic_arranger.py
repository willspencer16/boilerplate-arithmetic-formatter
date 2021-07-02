def arithmetic_arranger(problems):
    first_row = []
    arithmetic_operator = []
    second_row = []
    dashes = []

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
                dashes.append("-" * (len(list[2]) + 1))
            else:
                dashes.append("-" * (len(list[0]) + 1))



        else:
            return "Error: Too many problems."
    
    arranged_problems = f"   {first_row[0]}      {first_row[1]}      {first_row[2]}      {first_row[3]}\n"\
                        f"{arithmetic_operator[0]} {second_row[0]}    {arithmetic_operator[1]}    {second_row[1]}"\
                        f"    {arithmetic_operator[2]} {second_row[2]}    {arithmetic_operator[3]}  {second_row[3]}\n"\
                        f"{dashes[0]}    {dashes[1]}    {dashes[2]}    {dashes[3]}"
    
    return arranged_problems