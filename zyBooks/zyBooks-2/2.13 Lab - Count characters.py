word = input()
char = word[0]
phrase = word[2:]

count = phrase.count(char)
# print("word inputed: {}, char: {}, phrase: {}\n{} appears {} times".format(word,char,phrase,char,count))
print(count)