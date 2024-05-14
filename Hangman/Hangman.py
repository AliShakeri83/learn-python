import random

lst = [
    "hello",
    "bay",
    "worlds",
    "teachers",
    "game",
    "play",
    "safe",
    "calculator",
    "homework",
    "beautiful",
    "water",
    "oil",
]
word = list(random.choice(lst))
word_char = list("-" * len(word))
print("-".join(word_char))

while True:
    if word_char.count("-") == 0:
        print("You are won")
        break

    char = input("Enter your char(q for quit): ")
    if char == "q":
        break
    if char in word:
        for i in word:
            if i == char:
                word_char[word.index(i)] = char
                word[word.index(i)] = " "
        print("".join(word_char))
    else:
        print("No Char in word")
