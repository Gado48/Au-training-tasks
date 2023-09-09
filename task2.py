x = input("Enter the text: ")

sentences = x.count(".") + x.count("!") + x.count("?")
words = len(x.split())

letters = 0
for char in x:
    if char.isalpha():
        letters += 1


L = (letters / words) * 100
S = (sentences / words) * 100

grade_level = 0.0588 * L - 0.296 * S - 15.8

if grade_level >= 16:
    print("Grade 16+")
elif grade_level < 1:
    print("before Grade")
else:
    print("Grade ", end="")
    print(round(grade_level))
