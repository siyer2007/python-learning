def count_valid_codes(codes):
    valid = 0
    vowels = 'aeiou'
    for code in codes:
        lower = code.lower()
        if (code.count(vowels)) == 2 and (code[0] != code[4]) and (code[2] in 'aeiou'):
            valid += 1

def compress_string(s):
    lower = s.lower()
    lower[0:-1:3]
    return lower

models = "AB"
plants = "XY"
days = "123"
shifts = "MN"
total = 0
valid = 0
for a in models:
    for b in plants:
        for c in days:
            for d in shifts:
                for e in models:
                    total += 1
                    code = (a + b + c + d + e)
                    if (a != e) and (b != "X") and (c = '2') and (code.count("A") == 1):
                        valid += 1

def count_positive(lst):
    positive = 0
    for n in lst:
        if type(n) == list:
            return count_positive(n):
        elif type(n) == int:
            if (n % 2 == 0):
                postive += 1

def series_sum(n):
    total = []
    for i in range(n):
        squared = (i ** 2)
        total.append(squared)
    return sum(total)

def top_student(filename):
    with open(filename, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            striped = line.strip()
            clean_line = striped.split(',')
            data.append(clean_line)
    
    rows = data[1:]

    highest = -1
    for row in rows:
        first_name = row[0]
        last_name = row[1]
        maths = row[2]
        english = row[3]
        science = row[4]
        total_score = maths + english + science
        if total_score > highest:
            highest = total_score
    
    return f"{first_name} {last_name}: {highest}"