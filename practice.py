numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for n in numbers:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")



number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for n in number:
    if n % 7 == 0:
        print(n, "is odd and Lucky 7!")
    elif n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")



total = 0
for i in range(1, 101):
    if i % 3 == 0:
         total += 1
    print(i)
print("the number of numbers divisbale by 3 is", total)


total = 0
for i in range(1, 201):
    if i % 3 == 0 and i % 5 == 0:
            total += 1
            print(i, "is FizzBuzz")
    elif i % 3 == 0:
        if i % 5 != 0:
            print(i, "is Fizz")
    elif i % 5 == 0:
        if i % 3 != 0:
            print(i, "is Buzz")
    else:
        print(i)


def print_multiple(n, m):
    total = 0
    for i in range(1, m + 1):
        multiplied = n * i
        if multiplied % 2 == 0:
            total += 1
        print(n, "x", i, "=", multiplied)
    print("Total even multiples", total)

#simple exam style questions

total = 0
for i in range(1, 51):
    if i % 4 == 0:
        if i % 6 == 0:
            total += 1
            print(i, "is QuadHex")
        else:
            print(i, "is Quad")
    elif i % 6 == 0:
        print(i, "is Hex")
print("the total number of QuadHex is", total)


def largest_odd(numbers):
    odd = []
    for n in numbers:
        if n % 2 != 0:
            odd.append(n)
    return max(odd)


def count_letters(string):
    vowels = 0
    consonants = 0
    for ch in string:
        if ch in 'aeiou':
            vowels += 1
        elif ch in 'qwrtyplkjhgfdszxcvbnm':
            consonants += 1
    print(vowels, consonants)


matrix_1 = sum(matrix[0])
matrix_2 = sum(matrix[1])
matrix_3 = sum(matrix[2])
total = matrix_1 + matrix_2 + matrix_3
print(total)
print(matrix_1, matrix_2, matrix_3)

sentence = input("Enter your sentence here: ")
def count_vowels(sentence):
    vowels = 0
    sentence = sentence.lower()
    for ch in sentence:
        if ch in 'aeiou':
            vowels += 1
    print("there are", vowels, "in your sentence")

def word_slice(word):
    word[0:2]

def sum_even(nums):
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
    print(sum[even])