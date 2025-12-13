def sum_to_n(n):
    if n == 0:
        return n
    else:
        return n + sum_to_n(n -1)
    
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)
    
def count_numbers(lst):
    total = 0
    for item in lst:
        if type(item) == list:
            total += count_numbers(item)
        else:
            total += 1
    return total

def sum_nested(lst):
    total = []
    for n in lst:
        if type(n) == list:
            total.append(sum_nested(n))
        else:
            total.append(n)
    return sum(total)

def max_nested(lst):
    numbers = []
    for n in lst:
        if type(n) == list:
            numbers.append(max_nested(n))
        else:
            numbers.append(n)
    return max(numbers)