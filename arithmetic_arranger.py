def arithmetic_arranger(problems):
    first_row = []
    arithmetic_operator = []
    second_row = []

    for x in problems:
        list = x.split()
        first_row.append(list[0])
        arithmetic_operator.append(list[1])
        second_row.append(list[2])
    
    layout = f"   {first_row[0]}      {first_row[1]}      {first_row[2]}      {first_row[3]}\n"\
            f"{arithmetic_operator[0]} {second_row[0]}    {arithmetic_operator[1]}    {second_row[1]}"\
            f"    {arithmetic_operator[2]} {second_row[2]}    {arithmetic_operator[3]}  {second_row[3]}\n"\
            f"-----    ------    ----    -----"
    
    return layout