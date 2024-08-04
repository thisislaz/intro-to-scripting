user_val = int(input())

# cond_str = ""
# if user_val < 0:
#     cond_str = "negative"
# else:
#     cond_str = "non-negative"

cond_str = "negative" if user_val < 0 else "non-negative"

print(user_val, 'is', cond_str)