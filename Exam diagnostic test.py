"Q1: What does the following function return?"
def mystery(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    return result

print(mystery("COMPUTATION"))
'''
The function loops through s and checks if it is an
even number, and if it is an even number it adds it to the result
and then returns the result, and finally prints the mystery function.
'''

"Q2"
def highest_score(dict):
    return max(dict[value])

"Q3"
letters = "AB"
digits = "12"
total = []
single_a = []
for a in letters:
    for b in digits:
        for c in letters:
            code = (a + b + c)
            total.append(code)
            if code.count("A") == 1:
                single_a.append(code)
print(len(total))
print(len(single_a))

'''
Q4: What does this funciton do?
This function loops through a list and counts all
the values in the list, and if there is another list
within that list (nested list), then it calls the
funciton on itself to loop through that nested list
which is essentially recursion.
'''

"Q5: 10   ps. i am just guessing this one"

'''
Q6: What are two things every python class usually has?
A dWhat the class is and the actions of the class.
'''

'''
Q7: What is 5! ?
It just means you have to times everything before and including 5 together.
1 x 2 x 3 x 4 x 5 = 120
'''

'''
Q8:
First I need to get the file in and read it, then use the .strip
function and the .split function and then start analysing the data.
Use the max() function to find the highest score.
I forgot how to create a new file and edit and stuff.
'''