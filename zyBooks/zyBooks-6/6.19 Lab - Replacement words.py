words = list(input().split())
sentence = list(input().split())

word_dict = {}
for index in range(len(words)):
    if index % 2 == 0:
        word_dict[words[index]] = words[index+1]

for index in range(len(sentence)):
    for k,v in word_dict.items():
        if sentence[index] == k:
            sentence[index] = v
print(" ".join(sentence))