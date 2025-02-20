def missing_number(num1):
    reminder = []
    str1 = ""
    while num1 > 0:
        rem = num1 % 10
        reminder.append(rem)
        num1 = num1 // 10
    
    for i in range(1, max(reminder)):
        if i not in reminder:
            str1 += str(i)

    return str1 + " missing"

print(missing_number(13))