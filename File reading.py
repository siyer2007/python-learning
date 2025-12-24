def top_student(filename):
    # open the file and organise the data
    with open(filename, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            striped_line = line.strip()
            clean_line = striped_line.split(',')
            data.append(clean_line)
    
    rows = data[1:]

    top_name = ""
    top_score = -1
    for row in rows:
        first_name = row[1]
        last_name = row[2]
        score = int(row[3])
        if score > top_score:
            top_score = score
            top_name = f"{first_name} {last_name}"
    return f"{top_name}: {top_score}"


def top_average_student(filename):
    with open(filename, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            striped_line = line.strip()
            clean_line = striped_line.split(',')
            data.append(clean_line)
    
    rows = data[1:]
    highest_average = -1
    top_students = []

    for row in rows:
        first_name = row[0]
        last_name = row[1]
        maths = int(row[2])
        english = int(row[3])
        science = int(row[4])
        average = (maths + english + science) // 3

        if average > highest_average:
            highest_average = average
            top_students = [f"{first_name} {last_name}"]
        elif average == highest_average:
            top_students.append(f"{first_name} {last_name}")

    return f"{', '.join(top_students)}: {highest_average}"


def top_student(filename):
    with open(filename, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            striped_line = line.strip()
            clean_line = striped_line.split(',')
            data.append(clean_line)
    
    rows = data[1:]

    top_score = -1

    for row in rows:
        first_name = row[0]
        last_name = row[1]
        maths = int(row[2])
        english = int(row[3])
        science = int(row[4])
        score = maths + english + science
        if score > top_score:
            top_score = score

def read_file(filename):
    with open(filename, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            striped = line.strip()
            clean_line = striped.split(',')
            data.append(clean_line)
    
    rows = data[1:]

    highest_score = -1
    for row in rows:
        first_name = row[0]
        last_name = row[1]
        maths = int(row[2])
        english = int(row[3])
        science = int(row[4])
        total = maths + english + science

        if total > highest_score:
            highest_score = total
    
    return f"{first_name} {last_name}: {highest_score}"

def top_department(filename):
    with open(filename, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            striped_line = line.strip()
            clean_line = striped_line.split(',')
            data.append(clean_line)
    
    rows = data[1:]

    totals = {}

    for row in rows:
        department = row[1]
        sales_amount = int(row[2])

        if department not in totals:
            totals[department] = 0
        totals[department] += sales_amount

    max_total = -1
    top_dept = ""

    for dept, total in totals.items():
        if total > max_total or (total == max_total and dept < top_dept):
            max_total = total
            top_dept = dept
    
    return f"{top_dept}: {max_total}"