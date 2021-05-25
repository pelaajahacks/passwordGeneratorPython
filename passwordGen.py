import random

words = []

for i in range(5):
	word = input(str(i) + " : ")
	words.append(word)

random.shuffle(words)
for i in words:
	print(i, end="")

print(random.randint(1, 50), end="")
