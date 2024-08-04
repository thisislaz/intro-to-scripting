user_score = 0
simon_pattern = input()
user_pattern  = input()

''' Your solution goes here '''
for i in range(len(simon_pattern)):
    if simon_pattern[i] == user_pattern[i]:
        user_score+=1
    elif simon_pattern[i] != user_pattern[i]:
        break


print('User score:', user_score)