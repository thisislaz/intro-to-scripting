# user_tweet = input()
#
# ''' Your solution goes here '''
# if "LOL" in user_tweet:
#     print('LOL means laughing out loud.')
# else:
#     print('No abbreviation.')

user_tweet = input()

decoded_tweet = user_tweet.replace("TTYL","talk to you later")
print(decoded_tweet)