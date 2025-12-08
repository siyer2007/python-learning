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