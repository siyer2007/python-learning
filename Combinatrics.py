letters = "ABC"
nums = "012"
plants = "XY"
condition = 0
possibilities = []
for a in letters:
    for b in nums:
        for c in letters:
            for d in plants:
                possibilities.append(a + b + c + d)
                if a == 'A' and d == 'Y':
                    condition += 1
print(possibilities)
print(condition)


letters = "ABCD"
months = "123"
years = "45"
pos = []
two_A = 0
for a in letters:
    for b in months:
        for c in years:
            for d in letters:
                for e in letters:
                    combined = a + b + c + d + e
                    pos.append(combined)
                    if combined.count('A') == 2:
                        two_A += 1
print(pos)
print(two_A)


models = "TRB"
days = "012345"
plants = "XYZ"
all = []
special = 0
for a in models:
    for b in plants:
        for c in days:
            for d in models:
                all.append(a + b + c + d)
                if (int(c) % 2 == 0) and (b != 'Z') and (a != d):
                    special += 1
print(all)
print(special)


letters = "WXY"
digits = "13579"
factories = "AB"
years = "24"
all = []
rare = 0
for a in letters:
    for b in digits:
        for c in years:
            for d in letters:
                for e in factories:
                    for f in letters:
                        combined = a + b + c + d + e + f
                        all.append(combined)
                        if (a != f) and (int(b) > int(c)) and (e == "A") and (combined.count('Y') == 2) and (int(c) % 2 == 0):
                            rare += 1
print(len(all), rare)