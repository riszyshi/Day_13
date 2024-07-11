sentence = input("Enter your sentence: ")
words = []
word = ""
trigger1, trigger2, trigger3 = ',', ':', ';'

for w in sentence:
    if w == trigger1 or w == trigger2 or w == trigger3:
        if word:
            words.append(word.replace(" ", ""))
            word = ""
    else:
        word += w
if word:
    words.append(word.replace(" ", ""))

print(words)