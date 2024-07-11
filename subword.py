sentence = input("Enter your word: ")
words = []
subwords = []
word = ""

for w in sentence:
    if w.isalpha():
        word += w
    elif not w.isalpha():
        if word:
            words.append(word)
        word = ""
if word:
    words.append(word)

for word in words:
    length = len(word)
    subword_length = max(1, length // 2)  # Just an example, split words into 2 parts or single letters
    subwords.extend([word[i:i+subword_length] for i in range(0, length, subword_length)])

print("Subwords:", subwords)