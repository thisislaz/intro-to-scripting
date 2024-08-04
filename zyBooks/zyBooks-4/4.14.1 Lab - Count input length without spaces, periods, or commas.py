"""
Given a line of text as input, output the number of characters excluding spaces, periods, or commas.
Ex: If the input is:
Listen, Mr. Jones, calm down.
the output is:
21
Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").
"""

user_text = input()
count=0

for i in range(len(user_text)):
    print(user_text[i])
    if user_text[i] != "," and user_text[i] != " " and user_text[i] != ".":
        count+=1
print(count)