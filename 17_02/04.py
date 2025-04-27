def calculate_average(*args):
    if not args:
        return "Строка пустая"
    sum_znach = 0
    len_znach = 0
    #stroka = str(args)
    for i in args:
        try:
            sum_znach += int(i)
            len_znach += 1
        except (ValueError, TypeError):
            continue
        
    return sum_znach/len_znach

print(calculate_average())
print(calculate_average(1, 2, 3, 4))
print(calculate_average("10", 20, "30", "abc"))

