def count_multiples(n, limit):
    count = 0
    for i in range(1, limit + 1):
        if i % n == 0:
            count += 1
    return count
print(count_multiples(3, 10))  # 3
print(count_multiples(5, 20))  # 4

def sum_even(limit):
    total = 0
    for i in range(1, limit + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_even(10))
print(sum_even(5))

def count_long_words(words, n):
    count = 0
    for word in words:
        if len(word) > n:
            count += 1
    return count
print(count_long_words(words, 3))
print(count_long_words(words, 5))

def sum_multiples(n, limit):
    total = 0
    for i in range(1, limit + 1):
        if i % n == 0:
            total += i
    return total
sum_multiples(3, 10)
sum_multiples(5, 20)

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(find_largest([3, 7, 2, 9, 4]))
print(find_largest([-5, -2, -10, -1]))

def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count
print(count_vowels("hello world"))
print(count_vowels("Python"))