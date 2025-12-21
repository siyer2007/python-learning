def average_score(scores):
    return sum(scores.values()) / len(scores)

def team_average(teams):
    total = []
    for i in teams:
        for n in i:
            total.append(n)
    return (sum(total)) / (len(total))

def count_special_students(codes):
    special = 0
    for code in codes:
        x = int(code[1]) + int(code[3])
        if (code.count('A') == 2) and (code[0] != code[-1]) and (x % 2 == 0):
            special += 1
    return special

def count_valid_codes():
    codes = []
    letters = ["A", "B", "C"]
    digits = ["1", "2", "3"]
    for a in letters:
        for b in digits:
            for c in letters:
                for d in digits:
                    codes.append(a + b + c + d)
    print(codes)

def count_special_numbers(lst):
    special 
    for i in lst:
        if type(i) == int:
            if (i % 2 == 0) or (i > 3):
                special.append(i)
        elif type(i) == list:
            return count_special_numbers(i)

model = ["X", "Y"]
plant = ["A", "B"]
day = ["1", "2", "3"]
shift = ["M", "N"]
elite = 0
for a in model:
    for b in plant:
        for c in day:
            for d in shift:
                for e in model:
                    code = a + b + c + d + e
                    if (a != e) and (b != "A") and (c != "2") and (code.count("Y") == 1):
                        elite += 1