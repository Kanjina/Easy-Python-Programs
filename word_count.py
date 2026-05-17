"""
This is a simple python program which inputs two strings and detects whether the second string
is within the first string. This program is case insensitive.
"""
Text = str(input("Enter a string: "))
word = Text.lower()
oo = str(input("Enter the word you want to find (case insensitive): "))
leng = len(oo)
o = oo.lower()
def word_count(o):
    count = 0
    for i in range(len(word) - leng + 1):
        w = word[i:i + leng]
        if w == o:
            count = count + 1
    return count
print(word_count(o))
