def arithmetic_arranger(problems):
    first_row = []
    arithmetic_operator = []
    second_row = []

    for x in problems:
        list = x.split()
        if len(problems) < 5:
            if len(list[0]) < 5:
                first_row.append(list[0])
            else:
                print("Error: Numbers cannot be more than four digits.")
                exit()

            if list[1] == "+" or "-":
                arithmetic_operator.append(list[1])
            else:
                print("Error: Operator must be '+' or '-'.")
                exit()
            
            if len(list[2]) < 5:
                second_row.append(list[2])
            else:
                print("Error: Numbers cannot be more than four digits.")
                exit()
        else:
            print("Error: Too many problems.")
            exit()
    
    arranged_problems = f"   {first_row[0]}      {first_row[1]}      {first_row[2]}      {first_row[3]}\n"\
            f"{arithmetic_operator[0]} {second_row[0]}    {arithmetic_operator[1]}    {second_row[1]}"\
            f"    {arithmetic_operator[2]} {second_row[2]}    {arithmetic_operator[3]}  {second_row[3]}\n"\
            f"-----    ------    ----    -----"
    
    return arranged_problems