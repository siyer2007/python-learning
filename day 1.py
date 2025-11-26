print("Hello")



x = 10
y = 12
print(x + y)



for i in range(1, 11):
    print(i)



n = float(input("Enter a number"))
if n >= 0:
    print("Positive")
elif n < 0:
    print("Not positive")



for i in range(1, 11):
    if i % 2 == 0:
        print("Even")
    else:
        print(i)



nums = [102, 70, 865, 6780, 13]
print(nums[0], nums[-1], len(nums))



nums = [3, 7, 2, 9, 4]
total = 0
for n in nums:
    total += n



words = input("Enter your words here: ").lower()
vowels = 0
for ch in words:
    if ch in "aeiou":
        vowels += 1
print(vowels)



nums = [12, 7, 9, 20, 3, 8]
even_nums = []
for n in nums:
    if n % 2 == 0:
        even_nums.append(n)
print(even_nums)



original = input("Enter your words here: ")
reverserd_str = ""
for ch in orginal:
    reversed_str = ch + reversed_str
print(reversed_str)