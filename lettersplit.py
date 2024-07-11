sentence = input("Enter your word: ")
words = []
word = ""

for w in sentence:
    if w.isalpha():
        word += w
        words.append(word)
        word = ""
    elif not w.isalpha():
            word = ""       

print(words)