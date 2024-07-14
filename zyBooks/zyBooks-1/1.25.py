user_int=input("Enter integer (32 - 126):\n")
user_float=input("Enter float:\n")
user_character=input("Enter character:\n")
user_string=input("Enter string:\n")
print(user_int,user_float,user_character,user_string)
rev = user_string+" "+user_character+" "+user_float+" "+user_int
print(rev)
print(user_int,"converted to a character is",chr(int(user_int)))